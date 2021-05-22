const SET_GL_INGREDIENT = "ingredient/SET_GL_INGREDIENT";
const UNSET_GL_INGREDIENT = "ingredient/UNSET_GL_INGREDIENT";
const REMOVE_GL_INGREDIENT = "ingredient/REMOVE_GL_INGREDIENT";
const SET_MEAL_GL_INGREDIENT = "ingredient/SET_MEAL_GL_INGREDIENT";
const UNSET_MEAL_GL_INGREDIENT = "ingredient/UNSET_MEAL_GL_INGREDIENT";

const setGLIngredient = (ingredient) => ({
  type: SET_GL_INGREDIENT,
  ingredient,
});

const unsetGLIngredient = (ingredient) => ({
  type: UNSET_GL_INGREDIENT,
  ingredient,
});

const removeGLIngredient = () => ({
  type: REMOVE_GL_INGREDIENT
});

const setMealGLIngredient = (mealIngredients) => ({
  type: SET_MEAL_GL_INGREDIENT,
  mealIngredients
});

const unsetMealGLIngredient = (mealIngredients) => ({
  type: UNSET_MEAL_GL_INGREDIENT,
  mealIngredients,
});

export const addIngredientToGroceryList = (ingredient) => async (dispatch) => {
  dispatch(setGLIngredient(ingredient))
}

export const removeIngredientFromGroceryList = (ingredient) => async (dispatch) => {
  dispatch(unsetGLIngredient(ingredient));
};

export const logoutGL = () => async (dispatch) => {
  dispatch(removeGLIngredient());
};

export const addMealIngredientsToGroceryList = (mealIngredients) => async (dispatch) => {
  dispatch(setMealGLIngredient(mealIngredients));
}

export const removeMealIngredientsFromGroceryList = (mealIngredients) => async (dispatch) => {
    dispatch(unsetMealGLIngredient(mealIngredients));
  };

const initialState = {}
export default function groceryList(state = initialState, action) {
    switch (action.type) {
      case SET_GL_INGREDIENT:
        state[action.ingredient.id] = action.ingredient;
        return { ...state };
      case UNSET_GL_INGREDIENT:
        delete state[action.ingredient.id] 
        return { ...state };
      case REMOVE_GL_INGREDIENT:
        return {};
      case SET_MEAL_GL_INGREDIENT:
        action.mealIngredients.forEach((ingredient) => {
          state[ingredient.ingredient.id] = ingredient.ingredient;
        });
        return { ...state };
      case UNSET_MEAL_GL_INGREDIENT:
        action.mealIngredients.forEach((ingredient) => {
          delete state[ingredient.ingredient.id]
        });
        return { ...state };
      default:
        return state;
    }
}