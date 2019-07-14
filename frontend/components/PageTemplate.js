import React, { useState, useEffect } from "react";
import { connect } from 'react-redux'
import Search from '../components/Search'
import Entry from '../components/Entry'
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

const LoadingBar = styled.div`
    height: 4px;
    width: 100%;
    position: relative;
    overflow: hidden;
    background-color: #ddd;

  :before {
    display: block;
    position: absolute;
    content: "";
    left: -200px;
    width: 200px;
    height: 4px;
  }

  .loading {
    background-color: #2980b9;
    animation: loading 2s linear infinite;
  }
  
  @keyframes loading {
      from {left: -200px; width: 35%;}
      50% {width: 20%;}
      to {left: 100%;}
  }
`

import { useRouter } from 'next/router'
import { withRouter } from 'next/router'
import Link from 'next/link'



function Home({ children, loading }) {
    // const [loadAnimation, setLoadAnimation] = useState(true);

    // useEffect(() => {
    //     if(!loading) {
    //         setTimeout(() => {
    //             setLoadAnimation(false)
    //         }, 2000)
    //     }
    // }, [loading])

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
        
        {/* <LoadingBar className={loading && 'loading'}/> */}

        {children}
    </div>
}

function mapStateToProps(state, props) {
    return {
        loading: state.loading
    }
}

export default connect(mapStateToProps, null)(Home)