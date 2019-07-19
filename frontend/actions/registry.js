import { web3 } from '../web3'

const registry = new web3.eth.Contract(
    require('../chain/Registry.json'),
    require('../chain/Registry.js')
)

export const LOAD_ENTRY_PROGRESS = 'LOAD_ENTRY_PROGRESS'
export const LOAD_ENTRY_COMPLETE = 'LOAD_ENTRY_COMPLETE'

export function loadEntry(title) {
    // registry.lookup(key) => entryId[]
    // entryId is stored offchain but let's store everything onchain for now
    
    return async (dispatch) => {
        dispatch({
            type: LOAD_ENTRY_PROGRESS,
            title
        })

        const key = web3.utils.keccak256(title)
        // debugger

        console.log(key)
        let evs = await registry.getPastEvents(
            'Put',
            { 
                filter: {
                    key
                },
                fromBlock: '0',
                toBlock: 'latest'
            }
        )

        const results = evs.map(ev => {
            const { url, creator, key, time } = ev.returnValues;
            return { url, creator, key, total: 0, time: time.toNumber() }
        })

        dispatch(loadEntryComplete(results))
    }    
}

function loadEntryComplete(results) {
    return {
        type: LOAD_ENTRY_COMPLETE,
        results,
    }
}

export const LOAD_NEWEST_ENTRIES_COMPLETE = 'LOAD_NEWEST_ENTRIES_COMPLETE'

export function loadNewestEntries() {
    return async dispatch => {
        // Ethereum don't support no goddamn string params in events!!!

        // let evs = await registry.getPastEvents(
        //     'NewEntry',
        //     {
        //         fromBlock: '0',
        //         toBlock: 'latest'
        //     }
        // )

        // const results = evs.map(ev => {
        //     return ev.returnValues.title
        // })

        // dispatch({
        //     type: LOAD_NEWEST_ENTRIES_COMPLETE,
        //     results
        // })
    }
}

function sortEntries(entries) {
    // sort by the EBSL weighted whatever
    // just load a big matrix, and cache it offline for later
    // but we have to load all trust relations
    // make a fucckton of calls to the chain

    // which is probably why it's best to update this matrix on chain from time to time 
    // so we can just call it and the node's already know
    
}

import { trackTx } from './txs'

export const ADD_TO_REGISTRY_PROGRESS = 'ADD_TO_REGISTRY_PROGRESS'

export function addToRegistry(title, url) {
    return async (dispatch) => {
        dispatch({
            type: ADD_TO_REGISTRY_PROGRESS,
            txhash: null
        })

        const accounts = await web3.eth.getAccounts()
        let ev = registry.methods.put(title, url).send({ from: accounts[0] })

        ev.on('transactionHash', txhash => {
            dispatch({
                type: ADD_TO_REGISTRY_PROGRESS,
                txhash
            })
            
            dispatch(trackTx(ev, txhash))
        })        
    }
}