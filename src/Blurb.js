import React, {useState, useEffect} from 'react';


function Blurb() { 

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
        <div className='blurb'>
            {data.test ? (
          data.test.map((test, i) => (
            <p key={i} className="data-item">{test}</p>
          ))
        ) : (
          <p>Loading...</p>
        )}
        </div>
      ); 

}

export default Blurb;