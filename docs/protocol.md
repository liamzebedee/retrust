protocol (b|t)rainstorm
=======================

*I'd call it a brainstorm, but it happened on the train (again).* 
Description of retrust protocol design - trust, reputation primitive, cryptoeconomic interaction design:

 * retrust is a protocol for the exchange of trust and the calculation of reputation attributes
 * consumers of the protocol create bonds of a personal and dapp-specific ERC20 token 
 * apps can incorporate such a token into their user experience to build systems based on worldwide reputation (network effects)
 * users build reputation from interaction with other users through the protocol
 * interaction takes the form of challenge-response staking of trust bonds
 * trust bonds can be revoked, which produces more adverse affect on reputation than simply not reciprocated
 * two-sided marketplaces: supply/demand price can be regulated by the reputation mechanism
 * reputation can be used to improve dapp experience wherein users interact with re-liability (the idea of bonds) without the economic cost of issuing a token

 * this introduces completely decentralised reputation coordination mechanisms without a third-party, using a blockchain and a reputation convergence algorithm (EBSL)
 * it is sybil-resisant as a result
 * for this, all trust bonds must be registered to a decentralised ledger.



reputation can be framed as a measure of the reliability of some quality of a user
for example, an uber driver's reputation is how reliable their personal transportation service is

the single influencing factor in a user's reputation is their appraisal by other users
the reputation of drivers is the facilitating factor of Uber's proposition: cheaper rides through the possibility of a worldwide trusted network

through 1) passengers and drivers rating each other reciprocally after each ride, and 2) placing a minimum on reputation to join/use Uber, the service is made possible

the uber marketplace is a self-regulating system:
the service being offered is transportation
the cost of that service is determined in a two-sided market of drivers and riders (makers/takers, askers/bidders, buys/sells)
the supply/demand is regulated by the reputation mechanism whereof uber is the trusted custodian



I noted before reputation is created through interactions between drivers/riders, but this is not entirely correct

the first ride of a driver, their reputation is the theoretical maximum of 5 stars
comparing a driver with an average of 4.7 stars over 2000 rides with a rider of 5 stars and 0 rides, it's intuitive that the first is more safe

[^probability: you could probably draw some parallel with probability of events here. if you model the probability distribution of the event of having a bad ride from a driver, it would peak lower for more rides/experiments. More on this later - a confusing analogy to insert here for most, helpful for some]

driver reputation is actually created initially when uber has vetted the driver onto their platform - by passing their criminal checks, inspecting their car, etc. - the driver is approved and their reputation is a 'default' 5 stars

I demark 'default' in quotes - because it is again a nuance to explore: if you consider the supply of rides: it is controlled by the driver's reputation. likewise, the demand of rides is gatekept by the user's reputation. when uber approves a driver into their system, they are creating a bond that links their reputation to that of the driver. likewise, when riders sign onto uber, their reputation is based in the verification of their credit card by uber. both processes for creating reputation rely in trust in uber

[^repuation marketplaces: is reputation a marketplace? two sides of a service marketplace like uber - supply and demand depend on uber creating the reputation of being a reliable transport provider for the demand-side market, and a source of income that is safe (re: minimal cost in terms of danger and repair) for the supply-side market. uber is created out of nowhere as a corp (itself incurring cost), and they incur costs (verification) to create the reputation of each individual driver/rider. when a driver/rider signs on with uber, they too incur an opportunity cost]


the cost to obtain this reputation is different to the cost of obtaining it from riders. the phenomena is that the supply/demand is not 50-50 - there are more riders than drivers at any given time. 
there are more potential demands for rides than drivers: keep in mind that a driver can only fulfill one ride at a time, whereas there can be much outstanding demand for a ride
the reason being- being a driver is not as profitable as other jobs. it is good money in your spare time, but many can get a higher-paying or more rewarding job --- **relative** to the demand for rides from those who have a higher-paying job than a rider.

this is a basic economic concept of opportunity cost - the 'profit' forgone between two opportunities. in the context of the uber marketplace - the constraint is that you cannot be a rider and a driver at the same time - thus, participating in the market, there is an opportunity cost of (participating as a supplier of rides or a demander of rides).

and so, uber also has the surge mechanism - which is an exaxmple of mechanism design. surge increases the costs of rides when there is high demand, in order to incentivise more drivers to increase supply. it is a smart mechanism, and although lacking in data, I believe it performs its job well in larger contexts (e.g. NYE)

which brings me to my thesis of this section: the reputation mechanism of uber is an example of the general case that **reputation is a measure of the reliability of some quality of a user** - in this case, uber reputation is a measure of the reliability of a driver/rider in their supply/demand of the uber service: being a good rider or a good driver. the repeat liability (re-liability) being incurred is their opportunity cost of participation in this marketplace - for a driver, that means their source of income, for a rider, that means cheap mintos-laden rides to airports around the world!



## generalisation of default reputation
uber is a two-sided marketplace, but n=2 in a transaction is more an artifact of bureaucratic cost than a modern constraint.

when two users interact, trust is created. 
reputation is a function of trust

using a logical form, if you consider the rep of an uber driver with n rides and average rating x as driver(n, x), and similarly the rep of an uber rider rider(n, x)

reputation(driver(n=0, x=0)) = endorsement from uber = 5
reputation(rider(n=0, x=0))  = endorsement from uber = 5

drivers and riders begin with a default of 5
this default is in fact created from uber's trust in them (after verifying things)
and only valued by the pariticpants in the marketplace because of their trust in uber

### reputation as endorsement
we define the endorsement from uber in terms of reputation

in this reputation universe, the endorsement from uber is an independent action = it is not conditional on the reputation of other drivers/riders

the intention to supply/demand from the marketplace involves putting trust in uber to begin with. we consider brand trust as an aspect in the price signal of uber, and drivers/riders staying on their platform - 

HOWEVER why do we not have transportable reputation? uber is simply only a marketplace. we can look at the reputation of a lyft driver and come to similar terms on its value to us. 

we also place trust in uber to administer the reputation correctly. their proceses for verifying drivers must be safe, and the 
