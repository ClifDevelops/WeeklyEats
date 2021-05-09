import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllMeals } from "../../store/meal";
import "./Meals.css";

const Meals = () => {
    const dispatch = useDispatch()
    const meals = useSelector(state => state?.meal?.meals)
    // console.log(meals)
    useEffect(() => {
        dispatch(getAllMeals())
    }, [])

    return (
        <div>
            {meals?.map((meal) => {
                return (
                  <div key={meal.id} className="meal-individual-card">
                    <div><NavLink to={`/meals/${meal.id}`}>{meal.name}</NavLink></div>
                    <div>{meal.cuisine}</div>
                    <div>{meal.recipe}</div>
                    <button>Add to Grocery List</button>
                    <button>Add ingredients to meal</button>
                  </div>
                );
            })}
        </div>
    )
}

export default Meals