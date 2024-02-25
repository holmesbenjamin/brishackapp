import React, { useState, useEffect, useCallback, useRef } from "react";
import Webcam from "react-webcam";
import Button from "./Button";
// import './App.css';
function Camera() {
  const [img, setImg] = useState(null);
  const webcamRef = useRef(null);
  const capture = useCallback(() => {
    console.log("cunt");
    const imageSrc = webcamRef.current.getScreenshot();
    console.log(imageSrc);
    handleSubmit(imageSrc);
    setImg(imageSrc);
  }, [webcamRef]);
  const refresh = useCallback(() => {
    console.log("fag");
    setImg(null);
  }, []);

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
    console.log(json);
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
          <img src={img} className="img" alt="captured" />
          <button onClick={refresh}>Reset</button>
        </>
      )}
    </>
  );
}

export default Camera;
