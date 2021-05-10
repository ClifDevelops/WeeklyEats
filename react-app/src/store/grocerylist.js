const SET_GL_INGREDIENT = "ingredient/SET_GL_INGREDIENT";

const setIngredient = (ingredient) => ({
  type: SET_GL_INGREDIENT,
  ingredient,
});

export const addIngredientToGroceryList = (ingredient) => async (dispatch) => {
    dispatch(setIngredient(ingredient))
}

const initialState = {groceryList: []}
export default function groceryList(state = initialState, action) {
    switch (action.type) {
      case SET_GL_INGREDIENT:
        state.groceryList.push(action.ingredient);
        return { ...state };
      default:
        return state;
    }
}