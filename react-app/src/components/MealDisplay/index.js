import React from "react";
import { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getMealDetail } from "../../store/meal";
import { deleteFromGroceryList, addToGroceryList } from "../../store/grocerylist";
import { getAllIngredients } from "../../store/ingredient";
import MealIngredientsForm from "../MealIngredientsForm";

const MealDisplay = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const { mealId } = useParams();
    const meal = useSelector(state => state?.meal[mealId])
    const ingredients = useSelector((state) => state?.ingredient?.ingredients);
    console.log(meal)


    useEffect(() => {
        dispatch(getAllIngredients())
    }, [])

    if (!meal){
        history.push('/meals')
    }
    return (
        <div>
            <div className='meal-display-container'>
                <div>{meal?.name}</div>
                <div>Cuisine: {meal?.cuisine}</div>
                <div> RECIPE</div>
                <div>{meal?.recipe}</div>
                <button> Edit Meal</button>
                <button> Add ingredients to meal </button>
            </div>
            <MealIngredientsForm />
        </div>
    )

}

export default MealDisplay