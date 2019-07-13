import React, { useState } from "react";
import { connect } from 'react-redux'
import Search from '../components/Search'
import Entry from '../components/Entry'
import Contribute from '../components/Contribute'
import UserProfile from '../components/UserProfile'

import styled from 'styled-components';


const AppTitle = styled.h1`
    text-transform: lowercase;
    font-family: 'Audiowide', cursive;
    color: #333;
    align-self: center;
    flex: 1;
    padding-right: 1em;
    padding-left: 1em;
    font-size: 16px;

    :hover {
        cursor: pointer;
    }
`
const HeaderBar = styled.div`
    padding: 2em;
    background: #eee;
    display: flex;
    flex-direction: row;
`

const Col = `
    display: flex;
    flex-direction: column;
    flex-flow: row wrap;
`
const ColL = styled.div`
    ${Col}
    justify-self: flex-start;
    flex: 1;
`
const ColR = styled.div`
    ${Col}
    justify-self: flex-end;
    justify-items: flex-end;
`

const Row = styled.div`
    display: flex;
    flex-flow: row wrap;
`

const SearchStyle = styled.div`
    flex: 1;
`


import { useRouter } from 'next/router'
import { withRouter } from 'next/router'
import Link from 'next/link'



function Home({ children }) {
    return <div>
        <HeaderBar>
            <ColL>
                <Row>
                    <Link href="/">
                        <AppTitle>Guac</AppTitle>
                    </Link>
                    <Search/>
                    
                </Row>
            </ColL>

            <ColR>
                <UserProfile/>
            </ColR>
        </HeaderBar>

        {children}
    </div>
}

function mapStateToProps(state, props) {
    return state;
}

export default connect(mapStateToProps, null)(Home)