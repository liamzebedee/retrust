import PageTemplate from '../components/PageTemplate'
import Button from '../components/Button'
import styled from 'styled-components';
import AddLinkContainer from '../components/AddLinkContainer';

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

function AddEntry({ category, url, submit }) {
    return <PageTemplate>
        <AddEntryStyle>
            <Title>Add link</Title>

            <p>Your contribution is stored <i>*forever*</i> and can't be removed.</p>
            
            <FormRow>
            <label>Entry name</label>
            <textarea type='text' placeholder="eg. Bitcoin: A Peer-to-Peer Electronic Cash System" value={category}/>
            </FormRow>

            <FormRow style={{ paddingTop: 0 }}>
            <label>URL</label>
            <textarea type='text' value={url} placeholder="https, magnet, torrent and ipfs links go here"/>
            </FormRow>

            <FormRow>
                <Button>
                    Submit
                </Button>
            </FormRow>
        </AddEntryStyle>

    </PageTemplate>
} 

export default AddLinkContainer