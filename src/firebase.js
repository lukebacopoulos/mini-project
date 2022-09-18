import firebase from "firebase/app"
import "firebase/database"

var firebaseConfig = {
    apiKey: "AIzaSyC2xEDb1rA2QuwGv2E5o7_fn-Zu65NeuV0",
    authDomain: "miniproject-70e72.firebaseapp.com",
    databaseURL: "https://miniproject-70e72-default-rtdb.firebaseio.com",
    projectId: "miniproject-70e72",
    storageBucket: "miniproject-70e72.appspot.com",
    messagingSenderId: "590594251681",
    appId: "1:590594251681:web:f1a944d37f2dd0cddb49e0",
    measurementId: "G-C2SPSW24S2"
};

firebase.initializeApp(firebaseConfig)
const databaseRef = firebase.database().ref()
export const notesRef = databaseRef.child("notes")
export default firebase