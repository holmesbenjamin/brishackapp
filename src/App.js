import React, {useState, useEffect} from 'react';

function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch('/test').then(
      (res) => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    <div>
        {data.test ? ( 
          data.test.map((test, i) => (
            <p key={i}>{test}</p>
          ))
        ) : (
          <p>Loading...</p>
        )}
    </div>
  );
}

export default App