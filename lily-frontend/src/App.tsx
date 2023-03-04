import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  const [petName, setPetName] = React.useState<string>('');

  React.useEffect(() => {
    // ... backend call goes here
    axios.get<string>('http://127.0.0.1:5000/pet')
      .then(response => setPetName(response.data));
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Lily's pet is called {petName}.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
