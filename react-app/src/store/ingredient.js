const SET_INGREDIENT = 'ingredient/SET_INGREDIENT'

const setIngredient = (ingredients) => ({
    type: SET_INGREDIENT,
    ingredients
})

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
    console.log(response2)
}

const initialState = {};
export default function ingredient(state = initialState, action) {
    switch (action.type) {
        case SET_INGREDIENT:
            return { ...state, ...action.ingredients};
        default:
            return state;
    }
}