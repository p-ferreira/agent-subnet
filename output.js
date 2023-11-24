import React, { useState, useEffect } from 'react';

const Header = () => (
  <header>
    <h1>Welcome to our Single Page Application</h1>
    <h2>Hello from the agent-metaverse side! Here is the result of my first experiment:</h2>
  </header>
);

const Main = () => {
  const [time, setTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);
    return () => {
      clearInterval(timer);
    };
  }, []);

  return (
    <main style={{ textAlign: 'center' }}>
      <p>This is the main section of our application.</p>
      <div style={{ backgroundColor: 'black', color: 'white', padding: '10px' }}>
        <h2>{time}</h2>
      </div>
    </main>
  );
};

const Footer = () => (
  <footer>
    <p>© 2022 Our Company. All rights reserved.</p>
    <p style={{ fontSize: '14px', fontStyle: 'italic', color: 'black' }}>Powered by synapse labs</p>
  </footer>
);

const App = () => (
  <div>
    <Header />
    <Main />
    <Footer />
  </div>
);

export default App;
