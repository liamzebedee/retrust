import { web3 } from '../web3'

const memberNft = new web3.eth.Contract(
    require('../chain/MemberNFT.json'),
    require('../chain/MemberNFT.js')
)

const guac = new web3.eth.Contract(
    require('../chain/GUACToken.json'),
    require('../chain/GUACToken.js')
)

const LOAD_USER = 'LOAD_USER'

export const LOAD_USER_PROGRESS = 'LOAD_USER_PROGRESS'
export const LOAD_USER_NOT_FOUND = 'LOAD_USER_NOT_FOUND'
export const LOAD_USER_COMPLETE = 'LOAD_USER_COMPLETE'

export function loadUser(id) {
    return async dispatch => {
        dispatch({
            type: LOAD_USER_PROGRESS
        })

        const accounts = await web3.eth.getAccounts()

        const evs = await memberNft.getPastEvents(
            'Transfer', 
            {
                filter: {
                    from: '0x'+'0'.repeat(40),
                    to: accounts[0]
                },
                fromBlock: '0'
            }
        )
        
        if(evs.length == 0) {
            dispatch({
                type: LOAD_USER_NOT_FOUND
            })
            return
        }

        const ev = evs[0]
        const userId = ev.returnValues._tokenId;

        // Load reputation
        let reputation = await guac.methods.balanceOf(
            userId
        )

        dispatch({
            type: LOAD_USER_COMPLETE,
            user: {
                id: userId,
                reputation,
                registered: new Date,
                posts: [],
                votes: []
            }
        })

        // load all posts user has made
        // load all votes user has made
        // load when user registered

        
    }
}

