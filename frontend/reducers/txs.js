import { TX_UPDATE } from '../actions/txs'

const initialState = {}

export default function txs(state = initialState, action) {
    switch(action.type) {
        case TX_UPDATE:
            return {
                ...state,
                [action.txhash]: action.info
            }
        default:
            return state
    }
}