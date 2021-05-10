import {createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from 'redux-thunk';
import session from './session'
import ingredient from './ingredient'
import meal from './meal'
import groceryList from './grocerylist'


const rootReducer = combineReducers({
    session,
    ingredient,
    meal,
    groceryList
});

let enhancer;

if (process.env.NODE_ENV === 'production') {
    enhancer = applyMiddleware(thunk);
} else {
    const logger = require('redux-logger').default;
    const composeEnhancers =
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
