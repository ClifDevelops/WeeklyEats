import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { logoutGL } from "../../store/grocerylist"
import { logoutMeals} from "../../store/meal"
import { logoutIngredients} from "../../store/ingredient"
import './LogoutButton.css'

const LogoutButton = () => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    await dispatch(logout());
    await dispatch(logoutGL());
    await dispatch(logoutMeals());
    await dispatch(logoutIngredients());

  };

  return <button onClick={onLogout} className='logout-button'>Logout</button>;
};

export default LogoutButton;
