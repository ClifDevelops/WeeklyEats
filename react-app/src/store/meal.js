const SET_MEAL = 'meal/SET_MEAL'
const GET_MEALS = 'meals/GET_MEALS'
const REMOVE_MEALS = 'meals/REMOVE_MEALS'

const setMeal = (meal) => ({
    type: SET_MEAL,
    meal
})

const getMeals = (meals) => ({
  type: GET_MEALS,
  meals,
});

const removeMeals = () => ({
  type: REMOVE_MEALS
})

export const getAllMeals = () => async (dispatch) => {
  const response = await fetch("/api/meals/");
  let response2 = await response.json();
  // console.log(response2)
  dispatch(getMeals(response2));
};

export const addToMeals = (meal) => async (dispatch) => {
    const response = await fetch('/api/meals/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(meal)
    })
    let response2 = await response.json()
    dispatch (setMeal(response2))
    // console.log(response2)
}
export const editMeal = (meal) => async (dispatch) => {
  const response = await fetch("/api/meals/edit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(meal),
  });
  let response2 = await response.json();
  dispatch(setMeal(response2));
  // console.log(response2)
};

export const logoutMeals = () => async (dispatch) => {
  dispatch(removeMeals());
}

export const addToMealIngredients = (mealIngredient) => async (dispatch) => {
  const response = await fetch("/api/meals/ingredient", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(mealIngredient),
  });
  console.log('MI POST RETURNED', response)
}

const initialState = {}
export default function meal(state = initialState, action) {
    switch (action.type) {
      case SET_MEAL:
        state[action.meal.id] = action.meal
          // state.meals.push(action.meal)
        return { ...state };
      case GET_MEALS:
        const allMeals = {}
        // console.log(action.meals.meals)
        action.meals.meals.forEach(meal => {
          allMeals[meal.id] = meal
        })
        // for (meal in allMeals){
        //   meals.push(meal)
        // }
        return {...allMeals};
      case REMOVE_MEALS:
        return {}
      default:
        return state;
    }
}