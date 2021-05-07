import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllIngredients } from "../../store/ingredient";
import "./AllIngredients.css";

const AllIngredients = () => {
    const dispatch = useDispatch()
    const ingredients = useSelector(state => state?.ingredient?.ingredients)
    console.log(ingredients)
    useEffect(() => {
        dispatch(getAllIngredients())
    }, [])

    return (
        <div>
            {ingredients?.map((ingredient) => {
                return (
                    <div key={ingredient[0]} className='ingredient-individual-container'>
                    <div>{ingredient.name}</div>
                    <div>{ingredient.type}</div>
                    {/* <div>{ingredient.measurementUnit}</div> */}
                    <button>Add to Grocery List</button>
                    </div>
                )
            })}
        </div>
    )
}

export default AllIngredients