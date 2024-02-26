import React, { useState, useEffect } from 'react';



function Blurb() {
  // Initialize data as an empty array
  const [data, setData] = useState([]);

  const fruitData = {
    'Apple Braeburn': {
      format: (item) =>
        `Apples, with around 95 calories per medium-sized fruit, boast essential vitamins like C and A, potassium, and dietary fiber, promoting immune function and heart health. `,
    },
    'Banana Lady Finger': {
      format: (item) =>
        `Bananas, containing about 105 calories per medium-sized fruit, are rich in vitamin B6, C, potassium, and manganese, supporting metabolism and bone health while aiding nerve function and heart health.`,
    },
    // Add other fruits with their formatting functions
  };

  const fetchData = async () => {
    try {
      const res = await fetch('/classify');
      const data = await res.json();
      setData(data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="blurb">
      {data.length > 0 ? (
        data.map((item, index) => {
          const formatFunction = fruitData[item.class]?.format;
          if (!formatFunction) {
            return (
              <p key={index} className="data-item">
                Unknown fruit: {item.class}
              </p>
            );
          }
          const formattedText = formatFunction(item);
          return <p key={index} className="data-item">{<b>{item.class}</b>}: {formattedText}</p>;
        })
      ) : (
        <p>Please scan a fruit...</p>
      )}
    </div>
  );
}

export default Blurb;
