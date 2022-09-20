import React, { useState } from 'react'
import './App.css';   // this is the file used for changing the ht
import TwitterHandles from './TwitterHandles'

import handles from './handles'

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

    </>     //fragment allows multiple arguments in return
  )
}

export default App;

