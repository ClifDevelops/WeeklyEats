import React from "react";
import { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getMealDetail } from "../../store/meal";
import { deleteFromGroceryList, addToGroceryList } from "../../store/grocerylist";

const MealDisplay = () => {
    const dispatch = useDispatch();
    const { id } = useParams();
    const meal = useSelector(state => state?.meal?.meals[id])
    console.log(meal)

    return (
        <div>{meal.name}</div>

    )

}

export default MealDisplay