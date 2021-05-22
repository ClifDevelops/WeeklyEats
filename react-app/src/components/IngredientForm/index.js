import React, { useState } from "react";
import { useDispatch } from "react-redux";

import { addToIngredients } from "../../store/ingredient"

import './IngredientForm.css'

const IngredientForm = () => {
    const dispatch = useDispatch();
    const [name, setName] = useState('');
    const [type, setType] = useState('dairy');
    


    const updateName = (e) => {
        setName(e.target.value)
    };

    const updateType = (e) => {
        setType(e.target.value)
    };

  

    const onSubmit = async (e) => {
        e.preventDefault();
        const ingredient = {
            name,
            type,
            
        }
       
        await dispatch(addToIngredients(ingredient))
        setName("");
        setType("dairy");
        
    }


    return (
      <div className="ingredient-form-container">
        <div className="ingredient-form-text">
          Don't see what you're looking for? Add a new ingredient here.
        </div>
        <form onSubmit={onSubmit}>
          <div>
            <input
              type="text"
              name="name"
              onChange={updateName}
              value={name}
              placeholder="Ingredient Name"
              className="ingredient-form-input"
            ></input>
          </div>
          <div>
            <select
              name="type"
              onChange={updateType}
              value={type}
              className="ingredient-form-input"
            >
              <option value="dairy">dairy</option>
              <option value="fat">fat</option>
              <option value="fruit">fruit</option>
              <option value="grain">grain</option>
              <option value="protein">protein</option>
              <option value="vegetable">vegetable</option>
              <option value="herb">herb</option>
              <option value="spice">spice</option>
              <option value="pantry staple">pantry staple</option>
            </select>
          </div>
          <button type="submit" className='ingredient-form-button'>Enter Ingredient</button>
        </form>
        
      </div>
    );


}

export default IngredientForm;