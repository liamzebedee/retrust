retrust
=======

[**\Checkout the compendium!**](https://docs.google.com/document/d/1Rg-GLxpxgVBYDTHEXvlAxMc4459E9j4BZME6Fj6deJo/edit)

Retrust is an R&D project into decentralised reputation. It uses an algorithm called [Evidence-Based Subjective Logic](https://arxiv.org/abs/1402.3319) (EBSL) for **subjective consensus** on governing value. It's sybil-resistant and oriented around a one-way flow of governing an ecosystem's norms and rewarding value creators based on a power-weighted consensus.

### The current inefficiency of TCR's
Token Curated Registries are an example of where Retrust can shine:
 * an ecosystem around curating a registry of information is created by issuing a token
 * staking incentivises highly-curated registries, as well as increasing value of the token
 * however - tokens are either fixed in supply, or issued by some sort of bonding curve. 
 * essentially, the token is used to mitigate sybil attacks, or the 'unfair' cultivation of power.

Essentially, we are using a token to achieve consensus on a subjective criteria (a *"good registry"*). The problem is that in order to curtail sybils from ruining the communal ecosystem value, we are limiting the ecosystem based on economics, rather than **generating value** we are **trading value**.

In Retrust, value is generated continuously according to the subjective consensus of shareholders. And in turn, the value you have contributed determines your sharepower. It is a one-way flow of governance that insures existing sharepower governs how the ecosystem grows its value. 

How do we ensure the value is kept 'sane'? How do we make sure the majority shareholder doesn't just sell their stake? This will vary from ecosystem to ecosystem, and I envision a variety of mechanisms will exist on top of sharepower - ie. staking which scales power according to time locked. 

The important contribution to understand is that we are inverting the mechanisms of governing. Rather than the token's value coming from the gameplay of the TCR, the TCR is governed by who created it and continues contributing value to it. 

## Organisation
 - `ebsl/` - evidence-based subjective logic implementations (original and my refactored version with Numpy)
 - `retrust/` - core mechanics of the protocol (interactions, quorum and reputation engines)
 - `simulation/` - code for simulating behaviour of the different engines
 - `contracts/` - Solidity smart contracts
 - `visualisation/` - matplotlib-based visualisation code, used within simulation/ and datasets/

## Experiment
Install [Anaconda](https://www.anaconda.com), which handles Python version and dependencies.

```
# Activate the Anaconda environment
conda activate

# Run simulation
python -m simulation.main
```

## Developments
In chronological order:

 - Software to build example graphs/networks for algorithmic experimentation (better than Gephi - can make more than one edge ie. a Multigraph) [repo](https://stackblitz.com/edit/visualgraph-editor) [live](https://visualgraph-editor.stackblitz.io/)
 - [Thoughts on train back from Web3 (Oct)](https://gist.github.com/liamzebedee/c1bb4f79b67b3e7a39215b7ac3a80771)
 - [Economic Leverage & Personal Currency, DAO's, Climate Change vehicle (Oct)](https://slides.com/liamzebedee/retrust)
 - [Background - Part 1 (Oct)](https://medium.com/@liamzebedee/deriving-a-reliable-trust-protocol-that-scales-to-the-planet-pt-1-d994835cb008)
 - [Simulations of trust flow algorithms (Nov)](https://colab.research.google.com/drive/1BITXYa-b8BOwmrKh0czSUzQVeOdTc0Uj)
 - [EBSL source (Nov)](https://gist.github.com/liamzebedee/1f5c56d656ceba808a2e99e78e9f6160)
 - [Protocol brainstorms (Dec)](https://hackmd.io/m8MARMuuRHKZFw9xyQIH9Q), [Reputation as economic mechanism (Dec)](https://hackmd.io/3UVGjqBhSDKsr85nYiiIsw)
 - [Evidence-Based Subjective Logic (EBSL) reimplemented in Python with Numpy (Dec)](https://github.com/liamzebedee/retrust/tree/3933ecf076a775d566d7a07349bd6d46f3c0e002/vis/trust2)
 - [Discussions with Abram Simons of BrightID (Dec)](https://www.reddit.com/r/idealmoney/comments/a9croi/deriving_a_reliable_trust_protocol_that_scales_to/)
 - Matplotlib animation of EBSL algorithm (`python -m visualisation.main`) - also see in `docs/algovis.mp4` (Jan 2019)
 - [Preliminary implementation](https://github.com/liamzebedee/retrust/commit/4f53c10b88a262c47bcf538830e2b2f802c19935) of the quorum mechanism with NetworkX's PageRank algo (Jan 2019)
 - Use case exploration with decentralised Uber (Jan 2019)
 - Shift from reputation into the more general concepts of risk, governance and subjective consensus. See this [lightpaper](https://docs.google.com/document/d/1qbESkHU984D4_uf1ghIDa4hPcaevtRBa0KqRJbZnR_w/edit?usp=sharing) (May 2019)

## Resources
 - “decentralized sybil resistant identity” at Devcon4. Read the [reputation jam tweetstorm](https://twitter.com/sinahab/status/1027640621110984704)
 - [Identity and reputation in Web3](https://sinahab.com/2018/09/identity-and-reputation-in-web-3/)
 - Sybil control using economic stake mechanisms in Bitcoin, from the inventor of Ethereum [Vitalik](https://www.reddit.com/r/btc/comments/9szwi4/happy_whitepaper_day_xd/e8xxf4g/?utm_content=permalink&utm_medium=front&utm_source=reddit&utm_name=btc): ...the idea itself contained multiple fundamental innovations (chain-based consensus and, more importantly, the use of economic resources for the dual functions of incentivization and sybil control in distributed systems) that have transformed the field.
 - Subjective logic has problems with the communicativity of its operators. EBSL looks good ([Flow-based reputation with uncertainty](https://arxiv.org/pdf/1402.3319.pdf))
 - Relative vs. Absolute trust measures. 
 - https://www.youtube.com/watch?v=ZbgDFXxmNuk
 - [Tribler's research on consensus trust](https://github.com/Tribler/tribler/issues/3357), [some simulations on 'personalised' PageRank](https://github.com/Tribler/tribler/issues/2805) ([code](https://github.com/alexander-stannat/Incremental-Pagerank))
 - Blockscience's [multi-class personalised PageRank](https://github.com/sourcecred/research/blob/master/references/multiclassPageRank.md)
 - [Ethereum Magician's thread](https://ethereum-magicians.org/t/forgiveness-reputation-and-transparency-what-are-the-questions/1881)
 - [Reputation Systems: Promise and Peril](http://kronosapiens.github.io/blog/2018/06/29/reputation-promise-peril.html)

### Applications
 - Proof of personhood https://github.com/protocol/research/issues/11
 - A Universal Basic Income token, in which every unique individual who registers receives some amount of tokens.
 - A secure and anonymous method of tracking unique visitors or users
 - Electronic Voting
 - scalable personal currency https://www.joincircles.net/
 - citizen's economic leverage
 - generic reputation without middlemen - Swarm City, Colony, Augur
 - P2P Scihub
 - reputation as an alternative to economic stake in eg. curation markets
 - education/accreditation platform (Mick)
 - reputation of news sources
 - beating fake reviews (eg Amazon)
 - crypto co-operatives based on the ideas of coliability

#### Related projects
 - [yKarma](https://github.com/rezendi/ykarma)
 - [sourcecred](https://sourcecred.io/)
