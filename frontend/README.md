Like Reddit, but can't be taken down!


How does it work?

* All your votes are cryptographically signed as records
* An algorithm runs which summarises these votes



How do you stop spam?

* spam is socially filtered
* much like the filter bubble of facebook, we model the user as having X attention, which can be distributed between different items
* the attention is convertible into ecosystem value when users submit content and vote on it
* the average attention of the ecosystem is used for moderation






* if users don't want a part anymore, they can liquidate their rep


* for your vote to count, you need to have reputation
* upon signing up and putting down a deposit, you get some initial reputation
* you get reputation by contributing content







We use reputation to curate a registry
Registration is linked to an external curve
which allows you to mint votepower

why? we don't want reputation to be liquid
it's an external risk
maybe in future, but for similarlity to existing web2.0 systems

so users earn reputation by doing things
posting entries and so forth



the good ol, inverting the idea solution




ie. 

instead of wondering how we can enforce custodiality over an asset class (reputation) that is fundamentally
dynamically valued

issue the asset based on rules that depend on the dynamic value

issue a share token
call it an ERC20
and an id token
a ERC721

stake the share token into proposals





DAO:
    bonding curve for power
    deposit money, receive power


users own liability until they pay it back
and some form of xy price invariant ie uniswap, wherein my poor actions, reflect poorly on you depending on my amount of work and your amount of work



votes get scaled as conviction-weighted
wherein to vote, you need to have rep

people vote on things and those things are weighted by conviction
ie posts

but also you can stake on decisions before they're ratified


stackoverflow
users vote on posts
votes make reputation for users
users get privileges by reputation



Ability
    Voting: REP > 10
    Moderation: REP > 1000
Stats
    REP
Activities
    Posting
    Voting  -> REP 


Make post -> Get voted on -> Generate rep -> Get ability for mods -> Moderate
    o            o              o                     x


mod ability is a policy
it depends on coverging the matrix



eg. 

opinion of user:
    reputation
    confidence






basically what we want to do 
is generate an ecosystem token

which can be used for 
1) request payments
2) payments of other ecosystem services


when someone makes a bunch of posts
on an entry with nothing thus far

it's ok


seekers - they identify good content before it's found, and upvote it 

we seek to grow the community
that means finding content
and when it's good, approving it
thus rewarding the posters with the token
if they get enough of the token, they then become moderating bodies

https://stackoverflow.com/help/whats-reputation
https://stackoverflow.blog/2009/05/18/a-theory-of-moderation/
https://www.reddit.com/r/ethereum/
https://github.com/commons-stack/genesis-contracts/blob/master/contracts/bondingcurve/CommonsToken.sol
https://dzone.com/articles/harberger-taxes-on-ethereum


https://ethresear.ch/t/erc20-backward-compatible-gas-abstraction-using-constantinoples-eip-1014/4798


a brief plan:

you want to be able to pay for live access to requests
so you build a requests page
where you can stake some token

you can dispute entries


you just need mechanisms for minting the tokens

mechanisms for staking and reorg'ing the index
mechanisms for tagging content

what are the tokens useful for? 

when people want to join the community
they have to have stake to generate rep
and likewise

there is some form of curve available


there should be a built in uniswap pool for this purpose

what are we using? 
- conviction voting (to make proposals worth something)
- rep-based moderation curves
- time-based reward staking

make collective action better than individual
ie. uniswap pool, provide X% of power in return for growth




What is the goal?

to be able to get access to any stream for something

how can we do this?
- uncensorable decentralised registry
- mitigating sybil spam by reputation mechanisms
- integrating streaming 
- integrating paid-for requests (papers, shows, etc.)
- building in moderation tools


what are unresolved challenges?
- metamask tx for every vote = shit
- UX of querying index: autocomplete (wanted), showing recent entries (desired)


brainstorming:
- use meta transactions for users (eh)
- pay for all user transactions initially (eh2)
- put it all on SSB and have a trusted relayer summarise (eh3)    https://github.com/ssb-junkyard/ssb-feed
- own private ganache chain 
- loom sidechain
- some other L2 shit

what's best for ux?
- moderators: just do your job
- uploaders: also just do my job

so let's require metamask at a minimum and go with it








how can we build this UI?
the index

what can we do about the content? 



what if we have different stations
ie. request station - where you can make a request
ie. stream station - where you can ask for a stream

