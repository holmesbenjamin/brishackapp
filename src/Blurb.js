import React, {useState, useEffect} from 'react';


function Blurb(props) { 

  const [data, setData] = useState([{}]);

  // useEffect(() => {
  //   fetch('/test')
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setData(data);
  //       console.log(data);
  //     });
  // }, []);

  return (
        <div className='blurb'>
          <p>{props.text}</p>
        </div>
      ); 

}

export default Blurb;