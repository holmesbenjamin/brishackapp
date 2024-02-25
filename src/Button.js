import React, { useState, useEffect, useCallback } from 'react';
import './App.css';
import button from './Button.svg';

function Button(props) {
    const callback = useCallback(props.callback, [])
    return <img src={button} className='button' onClick={callback} />;
}  

export default Button