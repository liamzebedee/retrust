const LOAD_USER = 'LOAD_USER'

export const LOAD_USER_PROGRESS = 'LOAD_USER_PROGRESS'
export const LOAD_USER_COMPLETE = 'LOAD_USER_COMPLETE'

export function loadUser(id) {
    return async dispatch => {
        dispatch({
            type: LOAD_USER_PROGRESS
        })
        // load all posts user has made
        // load all votes user has made
        // load when user registered

        dispatch({
            type: LOAD_USER_COMPLETE,
            user: {
                id,
                reputation: 100,
                registered: new Date,
                posts: [],
                votes: []
            }
        })
    }
}

