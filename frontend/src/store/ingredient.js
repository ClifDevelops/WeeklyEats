const SET_INGREDIENT = 'ingredient/SET_INGREDIENT'
const GET_INGREDIENTS = 'ingredients/GET_INGREDIENTS'
const REMOVE_INGREDIENTS = "ingredients/REMOVE_INGREDIENTS";
const DELETE_INGREDIENT = 'ingredients/DELETE_INGREDIENT'

const setIngredient = (ingredient) => ({
    type: SET_INGREDIENT,
    ingredient
})

const getIngredients = (ingredients) => ({
    type: GET_INGREDIENTS,
    ingredients
})

const removeIngredients = () => ({
    type: REMOVE_INGREDIENTS
})

const deleteIngredient = (ingredient) => ({
    type: DELETE_INGREDIENT,
    ingredient
})

export const deleteFromIngredients = (ingredient) => async (dispatch) => {
    const response = await fetch("/api/ingredients/", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(ingredient),
    });
    let response2 = await response.json()
    dispatch(deleteIngredient(ingredient))
}

export const getAllIngredients = () => async (dispatch) => {
    const response = await fetch('/api/ingredients/')
    let response2 = await response.json()
    dispatch(getIngredients(response2))
    
}

export const addToIngredients = (ingredient) => async (dispatch) => {
    
    const response = await fetch('/api/ingredients/', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(ingredient)
    })
    let response2 = await response.json()
    dispatch(setIngredient(response2))
    
}

export const logoutIngredients = () => async (dispatch) => {
  dispatch(removeIngredients());
};

const initialState = {};
export default function ingredient(state = initialState, action) {
    switch (action.type) {
        case SET_INGREDIENT:
            const i_id = action.ingredient.id
            const ingredient_object = action.ingredient
            state[i_id] = ingredient_object
            
            return {...state};
        case GET_INGREDIENTS:
            
            action.ingredients.ingredients.forEach((ingredient) => {
                state[ingredient.id] = ingredient
            })
            
            return state;
        case REMOVE_INGREDIENTS:
            return {}
        case DELETE_INGREDIENT:
            console.log('here is that shit', action.ingredient.id)
            delete state[action.ingredient.id]
            return {...state}
        default:
            return state;
    }
}