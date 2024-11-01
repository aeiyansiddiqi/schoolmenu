// src/components/Menu.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Menu = () => {
  const [menuData, setMenuData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/menu') // Replace with your actual Flask API endpoint
      .then((response) => setMenuData(response.data))
      .catch((error) => console.error('Error fetching menu data:', error));
  }, []);

  if (!menuData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Weekly Menu</h1>
      {Object.entries(menuData).map(([day, meals]) => (
        <div key={day}>
          <h2>{day}</h2>
          {Object.entries(meals).map(([mealTime, items]) => (
            <div key={mealTime}>
              <h3>{mealTime}</h3>
              <ul>
                {items.map((item, index) => <li key={index}>{item}</li>)}
              </ul>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Menu;
