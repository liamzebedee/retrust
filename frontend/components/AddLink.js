import PageTemplate from '../components/PageTemplate'
import Button from '../components/Button'
import styled from 'styled-components';
import { useState } from 'react'
import TxStatusWidget from './TxStatusWidget'

const Title = styled.h2`
    font-size: 24px;
`

const AddEntryStyle = styled.div`
    margin: 3em auto;
    width: 600px;
`

const FormRow = styled.div`
display: flex;
justify-content: flex-end;
padding: 1em 0;

:nth-child(1) {
    padding-top: 0;
}
flex-direction: column;

label {
    padding: .5em 1em .5em 0;
    flex: 1;
    font-weight: bold;
}

input {
    height: 50px;
}
textarea {
    outline: none;
    resize: none;
    overflow: auto;

    border: 1px solid #333;
    padding: 1em;
}
`

const URLInput = styled.input`
    height: 75px;
`

function AddLink({ submit, txhash }) {
    let [title, setTitle] = useState()
    let [url, setUrl] = useState()
    let [submitted, setSubmitted] = useState(false)

    function startSubmit() {
        setSubmitted(true)
        submit(title, url)
    }

    return <PageTemplate>
        <AddEntryStyle>
            <Title>Add link <i className="fas fa-link"></i></Title>

            <p>Your contribution is stored <i>*forever*</i> and can't be removed.</p>
            
            <FormRow>
            <label>Entry name</label>
            <textarea type='text' onChange={ev => setTitle(ev.target.value)} placeholder="eg. Bitcoin: A Peer-to-Peer Electronic Cash System" value={title}/>
            </FormRow>

            <FormRow style={{ paddingTop: 0 }}>
            <label>URL</label>
            <textarea type='text' value={url} onChange={ev => setUrl(ev.target.value)} placeholder="https, magnet, torrent and ipfs links go here"/>
            </FormRow>

            <FormRow>
                <Button onClick={startSubmit}>
                    Submit
                </Button>

                { submitted ? <TxStatusWidget txhash={txhash}/> : null }
            </FormRow>
        </AddEntryStyle>

    </PageTemplate>
} 

export default AddLink