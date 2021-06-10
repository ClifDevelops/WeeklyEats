import React, {useEffect} from "react";
import { useDispatch } from "react-redux";
import { getAllIngredients } from "../../store/ingredient";
import GroceryList from '../GroceryList'
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
                <div className='homepage-meals-text'>
                    {`Pick from the meals below to add to your grocery list!
                    (If you don't see the "add to grocery list" button, click into the meal and attach some ingredients.)`}
                </div>
                <Meals />
            </div>
            <div className='gl-container'>
                <GroceryList />
            </div>
        </div>
    )
}

export default Homepage