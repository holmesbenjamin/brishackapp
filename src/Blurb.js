import React, {useState, useEffect} from 'react';


function Blurb() { 

  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch('/classify')
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div className='blurb'>
      {data.length > 0 ? (
        data.map((item, i) => (
          <p key={i} className="data-item">{item.class}</p>
        ))
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
  
  
  

}

export default Blurb;