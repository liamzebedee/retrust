# This simulation demonstrates a couple aspects of Retrust
# - how reputation can be computed in a decentralised context
# - how we can trust certain authorities, called 'greenlight'ers, to perform functions within the system: reviewing the cars/background of drivers and riders
# - how we can use reputation to design the marketplace to exclude repeat poor drivers/riders
# - how we can retroactively revoke trust of authorities, and recalibrate our worldview in a decentralised setting

# how can decentralisation improve this aspect?
# https://columbialawreview.org/content/the-taking-economy-uber-information-and-power/
# Some Evidence of Digital Market Manipulation in the Sharing Economy


# how is the sybil attack mitigated?
# ie. falsely inflating reputation by generating many interactions between random users
# 1) proof of identity - you can only register so many accounts, incurring a cost through the registrar
# 2) gps tracking - something like loom network can be used for proof of location during a trip
# 3) application logic - you cannot be driving 24-7-365, and users must be in a place for it to work



from usecases.uber.users import *

from retrust.interactions import InteractionsEngine
from ebsl.reputation import EBSLReputationEngine

from time import time
interactions = InteractionsEngine()
rep = EBSLReputationEngine(interactions)

from collections import namedtuple
import numpy as np


import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import os 

MarketAsk = namedtuple('MarketAsk', 'time rider')
MarketBid = namedtuple('MarketBid', 'time driver')

class Marketplace:
    def __init__(self):
        self.asks = []
        self.bids = []
    
    def ask_ride(self, rider):
        self.asks.append(MarketAsk(time(), rider))
    
    def offer_ride(self, driver):
        self.bids.append(MarketBid(time(), driver)) 
    
    def reputation(self, perspective=None, of=None):
        return 1
    
    def driver_rep(self, perspective=None, of=None):
        return 1
    
    def rider_rep(self, perspective=None, of=None):
        return 1

    def match(self):
        matches = []

        # ask for rides
        # bid for passenger

        riders_q = sorted(self.asks, key=lambda x: x.time)
        drivers_q = sorted(self.bids, key=lambda x: x.time)


        for (time, rider) in riders_q:
            for (time, driver) in drivers_q:
                # TODO need to incorporate the different greenlight trustees
                if self.reputation(perspective=driver, of=rider) > 0.5 and self.reputation(perspective=rider, of=driver) > 0.5:
                    # matches.append((
                    #     rider,
                    #     driver,
                    # ))
                    drivers_q.remove((time, driver))
                    matches.append((
                        rider,
                        driver,
                    ))
                    break

            # perform matches
            # thankfully this isn't like a normal market
            # in the sense that left and right can only be filled by one
            # except it is
            # even in this marketplace where everyone has rep
            # it's still from the perspective of each individual driver/rider

        self.asks = []
        self.bids = []

        for (rider, driver) in matches:
            interactions.insert([
                (rider.id, driver.id, 1),
                (driver.id, rider.id, 1)
            ])

            


            


uber = Marketplace()


drivers = [Driver() for x in range(10)]
riders = [Rider() for x in range(20)]


# Greenlight the drivers
greenlighters = [User() for x in range(4)]
for driver in drivers:
    interactions.insert([
        (driver.id, greenlighter.id, 1) for greenlighter in greenlighters
    ])

for rider in riders:
    interactions.insert([
        (rider.id, greenlighter.id, 1) for greenlighter in greenlighters
    ])


for i in range(16):
    for driver in drivers:
        if np.random.rand() > 0.2:
            uber.offer_ride(driver)

    for rider in riders:
        if np.random.rand() > 0.6:
            uber.ask_ride(rider)
    
    uber.match()
    rep.reload(interactions)

    fig, ax = plt.subplots()
    ax.matshow(rep.R[:,:,0], cmap=plt.cm.Blues)
    plt.savefig(f'{os.getcwd()}/{i}.repmatrix.png')

    print(i)

# rep.reload(interactions)

print(rep.R)