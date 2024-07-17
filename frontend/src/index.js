import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import "./styles.css"

export const URL = "http://127.0.0.1:8000/";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>
);


