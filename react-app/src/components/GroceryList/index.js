import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllMeals } from "../../store/meal";
import "./GroceryList.css";

const GroceryList = () => {


    return (
        <div className='grocery-list-container'> Here is the grocery list.</div>
    )
}

export default GroceryList