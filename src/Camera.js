import React, { useState, useEffect, useCallback, useRef } from "react";
import Webcam from "react-webcam";
// import './App.css';
function Camera() {
  const [img, setImg] = useState(null);
  const webcamRef = useRef(null);
  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImg(imageSrc);
  }, [webcamRef, setImg]);
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
          <button onClick={capture}>Capture</button>
        </>
      ) : (
        <>
          <img src={img} className="img" alt="captured" />
          <button
            onClick={() => {
              setImg(null);
            }}
          >
            Recapture
          </button>
        </>
      )}
    </>
  );
}

export default Camera;
