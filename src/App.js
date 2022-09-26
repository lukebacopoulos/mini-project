import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import TwitterHandles from './TwitterHandles'
import { Layout, Menu, Button, Breadcrumb, Icon } from 'antd';
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { gapi } from 'gapi-script';
import handles from './handles'

class App extends Component {


    constructor(props) {
        super(props)
        this.state = {
            list: []
        }
        this.handleClick = this.handleClick.bind(this)

    }



    handleClick() {
        let url = "http://127.0.0.1:5000/login?username=KyrieIrving"
        axios.get(url)
            .then(function (response) {
                let data = response.data
                alert(JSON.stringify(data));
            })
            .catch(function (error) {
                console.log(error);
            });
    }


    render() {
        return (
            <>

                <TwitterHandles handles={handles} />
                <input type="text" />
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

            </>
            
        );
    }
}

export default App;
