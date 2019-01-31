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



drivers = [Driver() for x in range(10)]
riders = [Rider() for x in range(30)]

class Marketplace:
    def __init__(self):
        self.asks = []
        self.bids = []
    
    def ask_ride(self, rider):
        self.asks.append(rider)
    
    def add_driver(self, driver):
        self.bids.append(driver)

    def match(self):
        # ask for rides
        # bid for passenger
        while 

uber = Marketplace()
map(uber.add_driver, drivers)



