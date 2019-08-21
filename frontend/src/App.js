import React from "react";
import {hot} from "react-hot-loader";
import Layout from "@/components/Layout"
import "./App.css";

class App extends React.Component {
    render(){
        return (
            <div className="App">
                <Layout />
            </div>
        );
    }
}

export default hot(module)(App);