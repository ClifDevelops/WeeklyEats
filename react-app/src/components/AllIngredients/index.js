import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { getAllIngredients } from "../../store/ingredient";
import {
  addIngredientToGroceryList,
  removeIngredientFromGroceryList,
} from "../../store/grocerylist";
import "./AllIngredients.css";
import IngredientForm from "../IngredientForm";
import GroceryList from "../GroceryList";

const AllIngredients = () => {
    const dispatch = useDispatch()
    
    useEffect(() => {
        dispatch(getAllIngredients());
    }, [])

    const ingredients = useSelector(state => state?.ingredient)
    const GL = useSelector(state => state?.groceryList)
   
    const [searchTerm, setSearchTerm] = useState("");
    
    useEffect(() => { 
    }, [Object.values(ingredients).length]);
    
    

    const addToGroceryList = (ingredient) => {
      dispatch(addIngredientToGroceryList(ingredient))

    }

    const removeFromGL = (ingredient) => {
      dispatch(removeIngredientFromGroceryList(ingredient));
    }
    
    return (
      <div className='ingredients-page-grid'>
        
        <div className="all-ingredients-container">
          <input
            className='ingredients-search-input'
            type="text"
            placeholder="Filter your ingredient options"
            onChange={(e) => {
              setSearchTerm(e.target.value);
            }}
          />
          {Object.values(ingredients)
            .filter((ingredient) => {
              if (searchTerm === "") {
                return ingredient;
              } else if (
                ingredient?.name
                  .toLowerCase()
                  .includes(searchTerm.toLowerCase()) ||
                ingredient?.type
                  .toLowerCase()
                  .includes(searchTerm.toLowerCase())
              ) {
                return ingredient;
              }
            })
            .map((ingredient) => {
              return (
                <div
                  key={ingredient.id}
                  className="ingredient-individual-container"
                >
                  <div>{ingredient.name}</div>
                  <div>{ingredient.type}</div>

                  {!GL[ingredient.id] ?
                  <button
                    className="ingredient-button"
                    onClick={() => addToGroceryList(ingredient)}
                  >
                    Add to Grocery List
                  </button> :
                  <button
                    className="removeGL-ingredient-button"
                    onClick={() => removeFromGL(ingredient)}
                  >
                    Remove from Grocery List
                  </button> }

                </div>
              );
            })}
        </div>
        <div className='ingredients-page-right-side-container'>
          <GroceryList />
        </div>
        <div className='ingredients-page-ingredient-form-container'>
          <IngredientForm />
        </div>
      </div>
    );
}

export default AllIngredients