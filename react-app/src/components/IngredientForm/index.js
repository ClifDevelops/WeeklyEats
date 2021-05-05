import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import { addToIngredients } from "../../store/ingredient"
import './IngredientForm.css'

const IngredientForm = () => {
    const dispatch = useDispatch();
    const [name, setName] = useState('');
    const [type, setType] = useState('');
    const [measurementUnit, setMeasurementUnit] = useState('');


    const updateName = (e) => {
        setName(e.target.value)
    };

    const updateType = (e) => {
        setType(e.target.value)
    };

    const updateMeasurementUnit = (e) => {
        setMeasurementUnit(e.target.value);
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        const ingredient = {
            name,
            type,
            measurementUnit
        }
        dispatch(addToIngredients(ingredient))
    }


    return (
      <form onSubmit={onSubmit}>
        <div>
          <input
            type="text"
            name="name"
            onChange={updateName}
            value={name}
            placeholder="Ingredient Name"
          ></input>
        </div>
        <div>
          <input
            type="text"
            name="type"
            onChange={updateType}
            value={type}
            placeholder="Ingredient Type"
          ></input>
        </div>
        <div>
          <input
            type="text"
            name="measurementUnit"
            onChange={updateMeasurementUnit}
            value={measurementUnit}
            placeholder="Measurement Unit"
          ></input>
        </div>
        <button type="submit">Enter Ingredient</button>
      </form>
    );


}

export default IngredientForm;