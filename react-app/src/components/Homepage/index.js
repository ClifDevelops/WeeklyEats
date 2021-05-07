import React from "react";
import { NavLink } from "react-router-dom";
import GroceryList from '../GroceryList'
import "./Homepage.css";

const Homepage = () => {
    return (
        <div className='homepage-container'>
            <div className='main-container'>Main component</div>
            <div className='gl-container'><GroceryList /></div>
        </div>
    )
}

export default Homepage