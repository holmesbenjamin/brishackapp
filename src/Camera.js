import React, {useState, useEffect} from 'react';
import Webcam from 'react-webcam';

function Camera () {
    
    return (
        <div>
            <Webcam width={854} height={480}/>
        </div>
    );
}

export default Camera