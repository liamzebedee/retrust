import { createStore, applyMiddleware } from 'redux'
import rootReducer from '../reducers'

const initialState = {
}

export function initializeStore() {
    const store = createStore(
        rootReducer
    )
    return store;
}