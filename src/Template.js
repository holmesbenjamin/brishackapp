// Import react
import React, {useState, useEffect} from 'react';


// 2. Create function
function Template () {

    // 3. Write some code to get data from backend
    // 3.1 Declare state variable
    const [data, setData] = useState([{}])
    // 3.2 Get data from backend
    useEffect( () => {
        // Function to get the data
        async function getData() {
            // 3.3 Input your API route here
            let data = await fetch('/test');
            let jsonData = await data.json();
            setData(jsonData);
        }
        getData();
    }, [])

    // 4. Return some JSX (html)
    return (<div>{data['key']}</div>);
}

// 5. Export function

export default Template