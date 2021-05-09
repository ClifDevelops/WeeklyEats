import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { addToIngredients } from "../../store/ingredient"
import AllIngredients from "../AllIngredients";
import './IngredientForm.css'

const IngredientForm = () => {
    const dispatch = useDispatch();
    const [name, setName] = useState('');
    const [type, setType] = useState('');
    // const [measurementUnit, setMeasurementUnit] = useState('');


    const updateName = (e) => {
        setName(e.target.value)
    };

    const updateType = (e) => {
        setType(e.target.value)
    };

    // const updateMeasurementUnit = (e) => {
    //     setMeasurementUnit(e.target.value);
    // };

    const onSubmit = async (e) => {
        e.preventDefault();
        const ingredient = {
            name,
            type,
            // measurementUnit
        }
        dispatch(addToIngredients(ingredient))
        setName("");
        setType("");
        // setMeasurementUnit("");
    }


    return (
      <div>
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
            <select name="type" onChange={updateType} value={type}>
              <option value="dairy">dairy</option>
              <option value="fat">fat</option>
              <option value="fruit">fruit</option>
              <option value="grain">grain</option>
              <option value="protein">protein</option>
              <option value="vegetable">vegetable</option>
            </select>
            {/* <input
            type="text"
            name="type"
            onChange={updateType}
            value={type}
            placeholder="Ingredient Type"
          ></input> */}
          </div>
          {/* <div>
          <input
            type="text"
            name="measurementUnit"
            onChange={updateMeasurementUnit}
            value={measurementUnit}
            placeholder="Measurement Unit"
          ></input>
        </div> */}
          <button type="submit">Enter Ingredient</button>
        </form>
        <AllIngredients />
      </div>
    );


}

export default IngredientForm;