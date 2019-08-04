import { LOGIN_USER } from "../actions/users";

const initialState = {
    loggedInUserId: null
}

function reduce(state = initialState, action) {
    switch(action.type) {
        case LOGIN_USER:
            return {
                ...state,
                loggedInUserId: action.id
            }
        default:
            return state
    }
}

export default reduce