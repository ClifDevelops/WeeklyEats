import React from "react";
import { NavLink, Redirect } from "react-router-dom";
import  { useDispatch, useSelector } from "react-redux";

import LoginForm from '../auth/LoginForm'
import SignUpForm from '../auth/SignUpForm'
import { login } from "../../store/session";
import "./Splash.css";

const Splash = () => {
const dispatch = useDispatch();
const user = useSelector(state => state.session.user);

const demoLogin = async (e) => {
    e.preventDefault();
    return await dispatch(login("Clif@Clif.com", "Clif"));
}

if (user) {
    return <Redirect to="/homepage" />;
}
    return (
        <div className='splash-container'>
            <div className='splash-title'>WeeklyEats</div>
            <div className='splash-forms-links-container'>
                <div> WeeklyEats is designed so that you customize the meals you typically like to eat and produce a shopping list of what you'll need for the week.</div>
                <div> Already a user? <NavLink to='/login' className='splash-links'>Login here</NavLink></div>
                <div> New user? <NavLink to='/signup' className='splash-links'>Signup</NavLink> or <button onClick={demoLogin} className="demo-user-button">
          {/* {" "} */}
          Or try as a demo user!
        </button></div>
                {/* <LoginForm /> */}
                {/* <SignUpForm /> */}
            </div>
            <div className='splash-banner-1'></div>

        </div>
    )
}

export default Splash;