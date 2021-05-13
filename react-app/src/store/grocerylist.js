const SET_GL_INGREDIENT = "ingredient/SET_GL_INGREDIENT";
const REMOVE_GL_INGREDIENT = "ingredient/REMOVE_GL_INGREDIENT";

const setGLIngredient = (ingredient) => ({
  type: SET_GL_INGREDIENT,
  ingredient,
});

const removeGLIngredient = () => ({
  type: REMOVE_GL_INGREDIENT,
});

export const addIngredientToGroceryList = (ingredient) => async (dispatch) => {
    dispatch(setGLIngredient(ingredient))
}

export const logoutGL = () => async (dispatch) => {
  dispatch(removeGLIngredient());
};

const initialState = {}
export default function groceryList(state = initialState, action) {
    switch (action.type) {
      case SET_GL_INGREDIENT:
        state[action.ingredient.id] = action.ingredient;
        return { ...state };
      case REMOVE_GL_INGREDIENT:
        return {} ;
      default:
        return state;
    }
}