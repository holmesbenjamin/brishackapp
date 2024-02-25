import React, { useState, useEffect } from "react";

function Blurb() {
  const [blurb, setBlurb] = useState([""]);

  return (
    <div className="blurb">
      <p>{blurb}</p>
    </div>
  );
}

export default Blurb;
