import { LOAD_USER_COMPLETE, LOGIN_USER } from '../actions/users'

const initial = {
}

function reduce(state = initial, action) {
    switch(action.type) {
        case LOAD_USER_COMPLETE:
            return {
                ...state,
                [action.user.id]: action.user
            }
        default:
            return state
    }
}

export default reduce