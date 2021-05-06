const SET_MEAL = 'meal/SET_MEAL'

const setMeal = (meal) => ({
    type: SET_MEAL,
    meal
})

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

const initialState = {meal: null}
export default function meal(state = initialState, action) {
    switch (action.type) {
        case SET_MEAL:
            return {...state, ...action.meal};
        default: 
            return state;
    }
}