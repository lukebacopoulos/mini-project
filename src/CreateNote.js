import React, { useState } from "react"
import { notesRef } from './firebase'

function CreateNote{
    const [note, setNote] = useStat("")

    const createNote = (e: React.FormEvent<EventTarget>) => {
        e.preventDefault()
        const item = {
            task: note
            done:false
        }
        noteRef.push(item)
        setNote("")
    }
    return (
        <form onSubmit={createNote}>
            <input type="text" value=<note> >
            )
}

export default CreateNote