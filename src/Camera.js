import React, { useState, useCallback, useRef } from "react";
import Webcam from "react-webcam";
import Button from "./Button";
import './App.css'; // Make sure to import the CSS file

function Camera() {
  const [img, setImg] = useState(null);
  const webcamRef = useRef(null);
  
  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImg(imageSrc);
  }, [webcamRef]);

  const refresh = useCallback(() => {
    setImg(null);
  }, []);

  // Here we add the 'img-greyed-out' class along with 'img'
  // to apply the greyed out effect on the captured image.
  const imageClassName = img ? "img img-greyed-out" : "img";

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
          <div className="img-wrapper"> {/* New wrapper with border */}
            <img src={img} className={imageClassName} alt="captured" />
          </div>
          <button onClick={refresh} className="reset-button">Reset</button>
        </>
      )}
    </>
  );
}

export default Camera;

