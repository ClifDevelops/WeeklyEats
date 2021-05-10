const SET_INGREDIENT = 'ingredient/SET_INGREDIENT'
const GET_INGREDIENTS = 'ingredients/GET_INGREDIENTS'

const setIngredient = (ingredient) => ({
    type: SET_INGREDIENT,
    ingredient
})

const getIngredients = (ingredients) => ({
    type: GET_INGREDIENTS,
    ingredients
})

export const getAllIngredients = () => async (dispatch) => {
    const response = await fetch('/api/ingredients/')
    let response2 = await response.json()
    dispatch(getIngredients(response2))
    // console.log(response2)
}

export const addToIngredients = (ingredient) => async (dispatch) => {
    console.log('HELOOOOOOOO', ingredient)
    const response = await fetch('/api/ingredients/', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(ingredient)
    })
    let response2 = await response.json()
    dispatch(setIngredient(response2))
    // console.log(response2)
}

const initialState = {ingredients: []};
export default function ingredient(state = initialState, action) {
    switch (action.type) {
        case SET_INGREDIENT:
            const i_id = action.ingredient.id
            const ingredient_object = action.ingredient
            state[i_id] = ingredient_object
            
            return { ...state};
        case GET_INGREDIENTS:
            const allIngredients = {}
            action.ingredients.ingredients.forEach(ingredient => {
                allIngredients[ingredient.id] = ingredient
            })
            console.log('here is state inside of get', state)
            return {...allIngredients};
        default:
            return state;
    }
}