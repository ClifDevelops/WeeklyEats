import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllIngredients } from "../../store/ingredient";
import { addIngredientToGroceryList} from "../../store/grocerylist";
import "./AllIngredients.css";

const AllIngredients = () => {
    const dispatch = useDispatch()
    const ingredients = useSelector(state => state?.ingredient)
    // console.log(ingredients)
    useEffect(() => {
        dispatch(getAllIngredients())
    }, [])

    const addToGroceryList = (ingredient) => {
        dispatch(addIngredientToGroceryList(ingredient))
    }
    return (
        <div>
            {Object.values(ingredients).map((ingredient) => {
                return (
                    <div key={ingredient.id} className='ingredient-individual-container'>
                        <div>{ingredient.name}</div>
                        <div>{ingredient.type}</div>
                        <button onClick={() => addToGroceryList(ingredient)}>Add to Grocery List</button>
                    </div>
                )
            })}
        </div>
    )
}

export default AllIngredients