const SET_GL_INGREDIENT = "ingredient/SET_GL_INGREDIENT";
const REMOVE_GL_INGREDIENT = "ingredient/REMOVE_GL_INGREDIENT";
const SET_MEAL_GL_INGREDIENT = "ingredient/SET_MEAL_GL_INGREDIENT";

const setGLIngredient = (ingredient) => ({
  type: SET_GL_INGREDIENT,
  ingredient,
});

const removeGLIngredient = () => ({
  type: REMOVE_GL_INGREDIENT,
});

const setMealGLIngredient = (mealIngredients) => ({
  type: SET_MEAL_GL_INGREDIENT,
  mealIngredients
});

export const addIngredientToGroceryList = (ingredient) => async (dispatch) => {
  dispatch(setGLIngredient(ingredient))
}

export const logoutGL = () => async (dispatch) => {
  dispatch(removeGLIngredient());
};

export const addMealIngredientsToGroceryList = (mealIngredients) => async (dispatch) => {
  dispatch(setMealGLIngredient(mealIngredients));
}

const initialState = {}
export default function groceryList(state = initialState, action) {
    switch (action.type) {
      case SET_GL_INGREDIENT:
        state[action.ingredient.id] = action.ingredient;
        return { ...state };
      case REMOVE_GL_INGREDIENT:
        return {} ;
      case SET_MEAL_GL_INGREDIENT:
        console.log("HERE ARE THE MEAL INGREDIENTS", action.mealIngredients)
        console.log("HERE IS THE INGREDIENT NAME", action.mealIngredients[0].ingredient.name)
        console.log(state)
        action.mealIngredients.forEach((ingredient) => {
          state[ingredient.ingredient.id] = ingredient.ingredient
        })
        return {...state }
      default:
        return state;
    }
}