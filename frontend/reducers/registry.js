import { ADD_TO_REGISTRY_PROGRESS } from '../actions/registry'

const initialState = {
    addToRegistry: null
}

export default function registry(state = initialState, action) {
    switch(action.type) {
        case ADD_TO_REGISTRY_PROGRESS:
            return {
                ...state,
                addToRegistry: action.txhash
            }
    }
    return state 
}