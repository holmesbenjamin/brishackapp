import React, { useState, useEffect } from "react";
import "./App.css";
import Camera from "./Camera";
import Blurb from "./Blurb";
import Logo from "./Logo";
import Button from "./Button";

function App() {

  const [blurb, setBlurb] = useState("Take a picture of a fruit to identify it.");

  const onLoad = () => {
    setBlurb("Loading...");
  };

  const onFinish = (data) => {
   setBlurb(data); 
  };




  return (
    <>
      <div className="app-container">
        <Logo />
        {/* <h1 className="app-title">FruitCam</h1>  */}
        <Camera onLoad={onLoad} onFinish={onFinish}/>
        <Blurb text={blurb}/>
      </div>
    </>
  );
}

export default App;
