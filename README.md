
Retrust is a WIP protocol for decentralised reputation/trust, based on [Evidence-Based Subjective Logic](https://arxiv.org/abs/1402.3319) (EBSL):
 * **Interaction-based**: reputation is based on generic interactions of the form, (source, target, value). There is no need to specify trusted friends/seeds, nor keep this information updated, as it is automatically derived from interactions.
 * **Application-agnostic**: reputation is a [subjective-logic opinion](https://en.wikipedia.org/wiki/Subjective_logic) of `(belief, disbelief, uncertainty)` - which can model any quality of reliability in interaction.

Properties still being investigated:
 * **Sybil-resistance**: a flow-based trust algorithm is computed from the perspective of each node.
 * **Quorum-based resolution**: interactions are converted to evidence in the form of `(positive, negative)` - it is likely possible we can use this to rank the effective trust of a node in a network, and thus use this to implement true holocratic voting.

## Organisation
 - `ebsl/` - evidence-based subjective logic implementations (original and my refactored version with Numpy)
 - `retrust/` - core mechanics of the protocol (interactions, quorum and reputation engines)
 - `simulation/` - code for simulating behaviour of the different engines
 - `contracts/` - Solidity smart contracts
 - `visualisation/` - matplotlib-based visualisation code, used within simulation/ and datasets/

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
 - Matplotlib animation of EBSL algorithm (`python -m visualisation.main`)

## Resources
 - “decentralized sybil resistant identity” at Devcon4. Read the [reputation jam tweetstorm](https://twitter.com/sinahab/status/1027640621110984704)
 - [Identity and reputation in Web3](https://sinahab.com/2018/09/identity-and-reputation-in-web-3/)
 - Sybil control using economic stake mechanisms in Bitcoin, from the inventor of Ethereum [Vitalik](https://www.reddit.com/r/btc/comments/9szwi4/happy_whitepaper_day_xd/e8xxf4g/?utm_content=permalink&utm_medium=front&utm_source=reddit&utm_name=btc): ...the idea itself contained multiple fundamental innovations (chain-based consensus and, more importantly, the use of economic resources for the dual functions of incentivization and sybil control in distributed systems) that have transformed the field.
 - Subjective logic has problems with the communicativity of its operators. EBSL looks good ([Flow-based reputation with uncertainty](https://arxiv.org/pdf/1402.3319.pdf))
 - Relative vs. Absolute trust measures. 
 - https://www.youtube.com/watch?v=ZbgDFXxmNuk
 - [Tribler's research on consensus trust](https://github.com/Tribler/tribler/issues/3357), [some simulations on 'personalised' PageRank](https://github.com/Tribler/tribler/issues/2805) ([code](https://github.com/alexander-stannat/Incremental-Pagerank))

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
 
