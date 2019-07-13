import { createStore, applyMiddleware, compose, combineReducers } from 'redux'
import reducers from '../reducers'
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';



// export const history = createBrowserHistory()
// export const history = !process.browser
//     ? createMemoryHistory({
//         initialEntries: ['']
//      })
//    : createBrowserHistory();

// const createRootReducer = (history) => combineReducers({
//     ...reducers,
//     // router: connectRouter(history),
// });
const composeEnhancers = composeWithDevTools({
    // Specify name here, actionsBlacklist, actionsCreators and other options if needed
  });


const initialState = {
}



export function configureStore(options) {
    const middleware = [
        thunk
    ]
    const store = createStore(
        reducers,
        initialState,
        composeEnhancers(
            applyMiddleware(...middleware),
        )
    )
    return store;
}