import React, { useState, useCallback, useRef } from "react";
import Webcam from "react-webcam";
import Button from "./Button";
import "./App.css"; // Make sure to import the CSS file

function Camera(props) {
  const [img, setImg] = useState(null);
  const webcamRef = useRef(null);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    console.log(imageSrc);
    handleSubmit(imageSrc);
    setImg(imageSrc);
  }, [webcamRef]);

  const reset = useCallback(() => {
    props.onReset();
    setImg(null);
  }, []);

  // Here we add the 'img-greyed-out' class along with 'img'
  // to apply the greyed out effect on the captured image.
  const imageClassName = img ? "img img-greyed-out" : "img";

  const handleSubmit = async (data) => {
    // console.log(data);

    props.onLoad();

    const response = await fetch("/upload", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    console.log("test");
    console.log(response.toString());
    let json = await response.json();
    console.log("test2");
    props.onFinish(json["upload"]);
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
          <button onClick={reset} className="reset-button">
            Reset
          </button>
        </>
      )}
    </>
  );
}

export default Camera;
