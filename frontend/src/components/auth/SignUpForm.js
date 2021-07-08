import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, NavLink } from 'react-router-dom';
import { signUp } from '../../store/session';
import './AuthForms.css'

const SignUpForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [errors, setErrors] = useState([]);

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password));
      
      if (data) {
        await setErrors(data);
        
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/homepage" />;
  }

  return (
    <div className='auth-page'>
      <form className="auth-form" onSubmit={onSignUp}>
        <div>
          {errors.map((error) => (
            <div key={error}>{error}</div>
          ))}
        </div>
        <div>
          <input
            type="text"
            name="username"
            onChange={updateUsername}
            value={username}
            placeholder="Username"
            className="auth-form-input"
          ></input>
        </div>
        <div>
          <input
            type="text"
            name="email"
            onChange={updateEmail}
            value={email}
            placeholder="Email"
            className="auth-form-input"
          ></input>
        </div>
        <div>
          <input
            type="password"
            name="password"
            onChange={updatePassword}
            value={password}
            placeholder="Password"
            className="auth-form-input"
          ></input>
        </div>
        <div>
          <input
            type="password"
            name="repeat_password"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
            placeholder="Confirm Password"
            className="auth-form-input"
          ></input>
        </div>
        <div>
          <button type="submit" className="auth-form-button">
            Sign Up
          </button>
          <NavLink to='/' className='auth-form-cancel-link'>Cancel</NavLink>
        </div>
      </form>
    </div>
  );
};

export default SignUpForm;
