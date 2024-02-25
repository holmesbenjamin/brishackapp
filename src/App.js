import React, { useState, useEffect } from 'react';
import './App.css'; 

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch('/test')
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div className="app-container">
      <h1 className="app-title">Zesty Fruits</h1> 
      <div className="data-display">
        {data.test ? (
          data.test.map((test, i) => (
            <p key={i} className="data-item">{test}</p>
          ))
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
}

export default App;
