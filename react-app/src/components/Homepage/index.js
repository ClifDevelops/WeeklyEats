import React, {useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllIngredients } from "../../store/ingredient";
import GroceryList from '../GroceryList'
import MealForm from '../MealForm'
import Meals from '../Meals'
import "./Homepage.css";

const Homepage = () => {
    const dispatch = useDispatch();
    
    useEffect(() => {
      dispatch(getAllIngredients());
    }, []);


    return (
        <div className='homepage-container'>
            <div className='main-container'>
                {/* <MealForm /> */}
                <Meals />
            </div>
            <div className='gl-container'>
                <GroceryList />
            </div>
        </div>
    )
}

export default Homepage