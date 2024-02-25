import React, { useState, useEffect, useCallback, useRef } from "react";
import Webcam from "react-webcam";
import Button from "./Button";
import './App.css'; // Make sure to import the CSS file

function Camera() {
  const [img, setImg] = useState(null);
  const webcamRef = useRef(null);
  const capture = useCallback(() => {
    // Removed inappropriate console log
    const imageSrc = webcamRef.current.getScreenshot();
    setImg(imageSrc);
  }, [webcamRef]);
  const refresh = useCallback(() => {
    // Removed inappropriate console log
    setImg(null);
  }, []);
  return (
    <>
      {img === null ? (
        <>
          <Webcam
            className="cam"
            mirrored={true}
            screenshotFormat="image/jpeg"
            ref={webcamRef}
          />
          <Button callback={capture} />
        </>
      ) : (
        <>
          <img src={img} className="img" alt="captured" />
          <button onClick={refresh} className="reset-button">Reset</button>
        </>
      )}
    </>
  );
}

export default Camera;

