import React, { useState } from "react";
import { search } from "../actions";
import { connect } from 'react-redux'
import Router from 'next/router'

import styled from 'styled-components';
const SearchBox = styled.input`
    width: 600px;
    height: 40px;
    padding: 0.25em 0.5em;
`

const Search = ({ dispatch }) => {
    const [searchQuery, setSearchQuery] = useState('')

    function onKeyPress(event) {
        if(event.key === 'Enter') {
            // dispatch(search(searchQuery))
            Router.push(`/entry/${searchQuery}`)
        }
    }

    return <div>
        <SearchBox 
            type='text' placeholder='Enter a search term here' 
            value={searchQuery} 
            onChange={e => setSearchQuery(e.target.value)}
            onKeyPress={onKeyPress}
        />
    </div>
}

function mapStateToProps(state) {
    return state;
}

export default connect(mapStateToProps)(Search)