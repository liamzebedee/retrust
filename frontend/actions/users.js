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

export const LOGIN_USER = 'LOGIN_USER'

function tupleToArray(obj) {
    return Object.values(obj)
}

export function loginUser(id) {
    return async dispatch => {
        dispatch({
            type: LOGIN_USER,
            id
        })
    }
}

export async function getUserInfo(id) {
    let data = await memberNft.methods.getData(id).call()
    let [ username, reputation ] = tupleToArray(data)
    reputation = reputation.toString()
    return {
        username,
        reputation
    }
}

export function loadUserInfo(id) {
    return async dispatch => {
        const userInfo = await getUserInfo(id)
        dispatch({
            type: LOAD_USER_COMPLETE,
            user: {
                id: id.toString(),
                ...userInfo
            }
        })
    }
}

import BN from 'bn.js'

export function loadUserForUsername(username) {
    return async dispatch => {
        let userId = await memberNft.methods.usernames(username).call()
        if(!userId) throw new Error('user not found')
        dispatch(loadUser(userId))
    }
}

export function loadAccounts() {
    return async dispatch => {
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

        evs.map(ev => {
            const userId = ev.returnValues._tokenId
            dispatch(loadUser(userId))
        })
    }
}

export function loadUser(id) {
    return async dispatch => {
        dispatch({
            type: LOAD_USER_PROGRESS
        })

        const accounts = await web3.eth.getAccounts()
        const owner = await memberNft.methods.ownerOf(id).call()

        const evs = await memberNft.getPastEvents(
            'Transfer', 
            {
                filter: {
                    from: '0x'+'0'.repeat(40),
                    to: owner
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

        let block = await web3.eth.getBlock(ev.blockHash)
        const userId = ev.returnValues._tokenId

        let userInfo = await getUserInfo(userId)
        

        dispatch({
            type: LOAD_USER_COMPLETE,
            user: {
                id: userId.toString(),
                ...userInfo,
                registered: block.timestamp,
                posts: [],
                votes: []
            }
        })

        // load all posts user has made
        // load all votes user has made     
    }
}

export function registerAccount() {
    return async dispatch => {
        const accounts = await web3.eth.getAccounts()
        const from = accounts[0]


        const depositAmount = await memberNft.methods.getMinimumDeposit().call()

        await memberNft.methods.join('foobar').send({ from, value: '50000000000000000' })
    }
}