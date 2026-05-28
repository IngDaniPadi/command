import { useState } from "react";

function App() {

  const [message, setMessage] = useState("");

  const turnOn = async () => {

    const response = await fetch("http://127.0.0.1:5000/on");

    const data = await response.json();

    setMessage(data.message);
  };

  const turnOff = async () => {

    const response = await fetch("http://127.0.0.1:5000/off");

    const data = await response.json();

    setMessage(data.message);
  };

  return (
    <div style={{
      textAlign: "center",
      marginTop: "100px",
      fontFamily: "Arial"
    }}>

      <h1>Patrón Command</h1>

      <button
        onClick={turnOn}
        style={{
          padding: "10px 20px",
          marginRight: "10px"
        }}
      >
        Encender
      </button>

      <button
        onClick={turnOff}
        style={{
          padding: "10px 20px"
        }}
      >
        Apagar
      </button>

      <h2>{message}</h2>

    </div>
  );
}

export default App;