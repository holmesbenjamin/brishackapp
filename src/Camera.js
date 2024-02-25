import React, { useState, useCallback, useRef } from "react";
import Webcam from "react-webcam";
import Button from "./Button";
import "./App.css"; // Make sure to import the CSS file

function Camera() {
  const [img, setImg] = useState(null);
  const webcamRef = useRef(null);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    console.log(imageSrc);
    handleSubmit(imageSrc);
    setImg(imageSrc);
  }, [webcamRef]);

  const refresh = useCallback(() => {
    setImg(null);
  }, []);

  // Here we add the 'img-greyed-out' class along with 'img'
  // to apply the greyed out effect on the captured image.
  const imageClassName = img ? "img img-greyed-out" : "img";

  const handleSubmit = async (data) => {
    console.log(data);
    const response = await fetch("/upload", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    let json = await response.json();
  };

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
          <div className="img-wrapper">
            {" "}
            {/* New wrapper with border */}
            <img src={img} className={imageClassName} alt="captured" />
          </div>
          <button onClick={refresh} className="reset-button">
            Reset
          </button>
        </>
      )}
    </>
  );
}

export default Camera