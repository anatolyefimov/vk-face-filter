import React from "react";
import "./App.css";

class App extends React.Component{
  render(){
    return(
      <div className="App">
        <h1> Hello, Worlds </h1>
      </div>
    );
  }
}

export default hot(module)(App);