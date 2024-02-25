import React, {useState, useEffect} from 'react';
import Webcam from 'react-webcam';
// import './App.css';
function Camera () {
    
    return (
        <div >
            <Webcam className='cam' width={854} />
        </div>
    );
}

export default Camera