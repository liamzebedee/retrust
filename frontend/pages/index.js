import React, { useState } from "react";
import { connect } from 'react-redux'
import Search from '../components/Search'
import Entry from '../components/Entry'

import styled from 'styled-components';


const AppTitle = styled.h1`
    text-transform: lowercase;
    font-family: sans-serif;
    color: #333;
    text-decoration: underline;
`
const HeaderBar = styled.div`
    padding: 2em;
    background: #eee;
`


function Home({ entry }) {
    return <div>
        <HeaderBar>
            <AppTitle>Weeki - a reputation-weighted wiki registry</AppTitle>
            <Search/>
        </HeaderBar>

        <Entry {...entry}/>
    </div>
}

function mapStateToProps(state, props) {
    return state;
}

export default connect(mapStateToProps, null)(Home)