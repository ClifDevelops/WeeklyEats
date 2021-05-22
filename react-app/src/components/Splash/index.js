import React from "react";
import LoginForm from '../auth/LoginForm'
import SignUpForm from '../auth/SignUpForm'
import "./Splash.css";

const Splash = () => {

    return (
        <div className='splash-container'>
            <div className='splash-title'>WeeklyEats</div>
            <div className='splash-forms-container'>
                <LoginForm />
                <SignUpForm />
            </div>
            <div className='splash-banner-1'></div>

        </div>
    )
}

export default Splash;