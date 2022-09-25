﻿import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

import { Layout, Menu, Button, Breadcrumb, Icon } from 'antd';

class App extends Component {


    constructor(props) {
        super(props)
        this.state = {
            list: []
        }
        this.handleClick = this.handleClick.bind(this)

    }

    handleClick() {
        let url = "http://127.0.0.1:5000/login?username=abcdef"
        axios.get(url)
            .then(function (response) {
                let data = response.data
                alert(data);
            })
            .catch(function (error) {
                console.log(error);
            });
    }


    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h1 className="App-title">Welcome to React</h1>
                </header>
                <p className="App-intro">
                    To get started, edit <code>src/App.js</code> and save to reload.
                </p>
                <Button onClick={this.handleClick}>search for twitter</Button>
            </div>
        );
    }
}

export default App;
