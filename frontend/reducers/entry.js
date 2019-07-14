import { LOAD_ENTRY_PROGRESS, LOAD_ENTRY_COMPLETE } from '../actions/registry'

const initial = {
    title: "",
    results: []
}

function reduce(state = initial, action) {
    switch(action.type) {
        case LOAD_ENTRY_PROGRESS:
            return {
                ...state,
                title: action.title
            }
        case LOAD_ENTRY_COMPLETE:
            return {
                ...state,
                results: action.results
            }
        default:
            return state
    }
}

export default reduce