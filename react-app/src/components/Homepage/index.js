import React from "react";
import { NavLink } from "react-router-dom";
import GroceryList from '../GroceryList'
import MealForm from '../MealForm'
import Meals from '../Meals'
import "./Homepage.css";

const Homepage = () => {
    return (
        <div className='homepage-container'>
            <div className='main-container'>
                <MealForm />
                <Meals />
            </div>
            <div className='gl-container'><GroceryList /></div>
        </div>
    )
}

export default Homepage