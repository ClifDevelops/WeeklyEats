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

const setMealGLIngredient = (meal) => ({
  type: SET_MEAL_GL_INGREDIENT,
  meal
});

const unsetMealGLIngredient = (meal) => ({
  type: UNSET_MEAL_GL_INGREDIENT,
  meal,
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

export const addMealIngredientsToGroceryList = (meal) => async (dispatch) => {
  dispatch(setMealGLIngredient(meal));
}

export const removeMealIngredientsFromGroceryList = (meal) => async (dispatch) => {
    dispatch(unsetMealGLIngredient(meal));
  };

const initialState = {mealsInGL: []}
export default function groceryList(state = initialState, action) {
    switch (action.type) {
      case SET_GL_INGREDIENT:
        state[action.ingredient.id] = action.ingredient;
        return { ...state };
      case UNSET_GL_INGREDIENT:
        delete state[action.ingredient.id] 
        return { ...state };
      case REMOVE_GL_INGREDIENT:
        state = {}
        state.mealsInGL = []
        return state;
      case SET_MEAL_GL_INGREDIENT:
        console.log('HERE I AM', state.mealsInGL)
        action.meal.meal_ingredients.forEach((ingredient) => {
          state[ingredient.ingredient.id] = ingredient.ingredient;
          // if (state[ingredient.ingredient.id]){

          // }
        });
        state.mealsInGL.push(action.meal.id)
        return { ...state };
      case UNSET_MEAL_GL_INGREDIENT:
        action.meal.meal_ingredients.forEach((ingredient) => {
          delete state[ingredient.ingredient.id];
        });
        const index = state.mealsInGL.indexOf(action.meal.id)
        if (index > -1) {
          state.mealsInGL.splice(index, 1);
        }
        return { ...state };
      default:
        return state;
    }
}