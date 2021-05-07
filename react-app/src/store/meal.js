const SET_MEAL = 'meal/SET_MEAL'
const GET_MEALS = 'meals/GET_MEALS'

const setMeal = (meal) => ({
    type: SET_MEAL,
    meal
})

const getMeals = (meals) => ({
  type: GET_MEALS,
  meals,
});

export const getAllMeals = () => async (dispatch) => {
  const response = await fetch("/api/meals/");
  let response2 = await response.json();
  dispatch(getMeals(response2));
  // console.log(response2)
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
    console.log(response2)
}

const initialState = {meals: []}
export default function meal(state = initialState, action) {
    switch (action.type) {
      case SET_MEAL:
          state.meals.push(action.meal)
        return { ...state };
      case GET_MEALS:
        return { ...action.meals };
      default:
        return state;
    }
}