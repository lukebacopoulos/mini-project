import React, { useState } from 'react'
import './App.css';   // this is the file used for changing the ht
import TwitterHandles from './TwitterHandles'
import { GoogleLogin } from 'react-google-login';
import { gapi } from 'gapi-script';
import handles from './handles'


const clientId = '454678718267 - gssejg95tm7qe49kgsfoib8g0uoj0tnn.apps.googleusercontent.com';
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
    console.log('success:', res);
};
const onFailure = (err) => {
    console.log('failed:', err);
};
return (
    <GoogleLogin
        clientId={clientId}
        buttonText="Sign in with Google"
        onSuccess={onSuccess}
        onFailure={onFailure}
        cookiePolicy={'single_host_origin'}
        isSignedIn={true}
    />
);

function App() {
  const [handles, addhandle] = useState([])
  return (
    <>
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

    </>     //fragment allows multiple arguments in return
  )
}

export default App;

