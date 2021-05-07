import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import LoginForm from '../auth/LoginForm'
import SignUpForm from '../auth/SignUpForm'
import "./Splash.css";

const Splash = () => {

    return (
        <div className='splash-container'>
            <div className='splash-forms-container'>
                <LoginForm />
                <SignUpForm />

            </div>

        </div>
    )
}

export default Splash;