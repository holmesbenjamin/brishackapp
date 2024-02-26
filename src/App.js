import React, { useState, useEffect } from "react";
import "./App.css";
import Camera from "./Camera";
import Blurb from "./Blurb";
import Logo from "./Logo";
import Button from "./Button";

function App() {
  const str = "Take a picture of a fruit to identify it";
  const [blurb, setBlurb] = useState(str);

  const onLoad = () => {
    setBlurb("Processing image...");
  };

  const onFinish = (data) => {
    setBlurb(data);
  };

  const onReset = () => {
    setBlurb(str);
  };

  return (
    <>
      <div className="app-container">
        <Logo />
        {/* <h1 className="app-title">FruitCam</h1>  */}
        <Camera onLoad={onLoad} onFinish={onFinish} onReset={onReset} />
        <Blurb text={blurb} />
      </div>
    </>
  );
}

export default App;
