export function isLoggedIn(state) {
    return state.user.loggedInUserId !== null
}

export function getUsersAvailable(state) {
    return Object.values(state.users).map(({ username, id }) => {
        return { username, id }
    }); 
    // TODO
}

export function getUserById(state, id) {
    return state.users[id]
}

export function getUser(state, username) {
    for(let user of Object.values(state.users)) {
        if(user.username == username) return user;
    }
    return null
}

export function loggedInUser(state) {
    let userId = state.user.loggedInUserId
    if(userId == null) {
        return {
            reputation: 1,
            registered: null,
            posts: [],
            votes: [],
            username: "()",
            userId,
        }
    }

    let user = state.users[userId]
    return user
}