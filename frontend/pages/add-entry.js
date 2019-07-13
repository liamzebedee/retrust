import PageTemplate from '../components/PageTemplate'
import Button from '../components/Button'
import styled from 'styled-components';


function AddEntry({ category }) {
    let url = ""

    return <PageTemplate>
        <h2>Add entry</h2>

        <p>Your entry is stored <i>*forever*</i> and can't be removed.</p>
        
        Category
        <input type='text' value={category} disabled/>

        URL
        <input type='text' value={url}/>

        <Button>
            Submit
        </Button>

    </PageTemplate>
} 

export default AddEntry