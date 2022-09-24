import './App.css';   // this is the file used for changing the ht
import TwitterHandles from './TwitterHandles'
import React, { useState, useEffect } from 'react';
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { gapi } from 'gapi-script';
import handles from './handles'



function App() {
    const [profile, setProfile] = useState([]);
    const clientId = '386932037035-k8v833noqjk7m4auae0t83vnkrqvvg3t.apps.googleusercontent.com';
    useEffect(() => {
        const initClient = () => {
            gapi.client.init({
                clientId: clientId,
                scope: ''
            });
        };
        gapi.load('client:auth2', initClient);
    });

    const onSuccess = (res) => {
        setProfile(res.profileObj);
    };

    const onFailure = (err) => {
        console.log('failed', err);
    };

    const logOut = () => {
        setProfile(null);
    };
    // api
    const [data, setdata] = useState({
        name: "",
        age: 0,
        date: "",
        programming: "",
    });
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/data").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    name: data.Name,
                    age: data.Age,
                    date: data.Date,
                    programming: data.programming,
                });
            })
        );
    }, []);

    
    return (
         <>
        <div>
            <h2>React Google Login</h2>
            <br />
            <br />
            {profile ? (
                <div>
                    <img src={profile.imageUrl} alt="user image" />
                    <h3>User Logged in</h3>
                    <p>Name: {profile.name}</p>
                    <p>Email Address: {profile.email}</p>
                    <br />
                    <br />
                    <GoogleLogout clientId={clientId} buttonText="Log out" onLogoutSuccess={logOut} />
                </div>
            ) : (
                <GoogleLogin
                    clientId={clientId}
                    buttonText="Sign in with Google"
                    onSuccess={onSuccess}
                    onFailure={onFailure}
                    cookiePolicy={'single_host_origin'}
                    isSignedIn={true}
                />
            )}
            </div>
            <TwitterHandles handles={handles} />
            <input type="text" />
            <button> Search Handle</button>

        <div>
              <h1>Bot or Real</h1>
          </div>
          <div>
              <h1>Main Topic</h1>
          </div>
          <div>
              <h1>Sentiment</h1>
            </div>

            <div className="App">
                <header className="App-header">
                    <h1>React and flask</h1>
                    {/* Calling a data from setdata for showing */}
                    <p>{data.name}</p>
                    <p>{data.age}</p>
                    <p>{data.date}</p>
                    <p>{data.programming}</p>

                </header>
            </div>
        </>

    );
}
export default App;
