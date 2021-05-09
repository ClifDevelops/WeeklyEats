import React from "react";
import { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getMealDetail } from "../../store/meal";
import { deleteFromGroceryList, addToGroceryList } from "../../store/grocerylist";

const MealDisplay = () => {
    const dispatch = useDispatch();
    const { id } = useParams();
    const meal = useSelector(state => state?.meal[id])
    console.log(meal)

    return (
        <div className='meal-display-container'>
            <div>{meal?.name}</div>
            <div>Cuisine: {meal?.cuisine}</div>
            <div> RECIPE</div>
            <div>{meal?.recipe}</div>
            <button> Edit Meal</button>
            <button> Add ingredients to meal </button>
        </div>

    )

}

export default MealDisplay