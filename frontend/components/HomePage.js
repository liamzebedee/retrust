import React, { useState } from "react";
import { connect } from 'react-redux'
import Search from './Search'
import Entry from './Entry'
import UserProfile from './UserProfile'

import styled from 'styled-components';
import PageTemplate from "./PageTemplate";
import Button from '../components/Button'

const AppTitle = styled.h1`
    text-transform: lowercase;
    font-family: 'Audiowide', cursive;
    color: #333;
    align-self: center;
    flex: 1;
    padding-right: 1em;
    padding-left: 1em;
    font-size: 16px;
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

const HeroBlock = styled.div`
    text-align: center;
    font-size: 22px;
`
const Hero = styled.h1`
font-size: 62px;
font-family: "Helvetica Neue", sans-serif;
line-height: 1.2;
color: rgb(51, 51, 51);
padding-top: 0em;
margin: 3rem;
margin-bottom: 1rem;
`

const CallToAction = styled.div`
a {
    color: black;
    text-decoration: none;
    :hover {
        opacity: 0.7;
    }
}
font-size: 80%;
`

const Padding = styled.span`
    padding: 0 .5em;
`

const Blocks = styled.div`
    display: flex;
    padding: 3rem;
    flex-direction: row;
    justify-content: space-evenly;
    margin: 0 3em;
`
const Block = styled.div`
    border: 1px solid #ddd;
    border-radius: 1px;
    padding: 1em;
    margin: 1em;
    flex: 1;
    box-shadow: 1px 1px #ddd;
    height: 250px;
    max-width: 350px;
    flex-spacing: space-around;
    font-size: 16px;
    p {
        line-height: 2;
    }

    h2 {
        line-height: 1.2;
    }
`

const FooterCtn = styled.div`
    flex: 1;
    flex-direction: column;
`

const Footer = styled.footer`
    text-align: center;
    flex: 1;
    flex-direction: column;


    a {
        color: black;
        text-decoration: none;
        :hover {
            opacity: 0.7;
        }
    }
`

const AddAnEntryCTA = styled.div`
    
    display: inline-block;
`

import Link from 'next/link'


function Home({ entry, misc }) {
    return <PageTemplate>
        <HeroBlock>
            <Hero>The unstoppable index.</Hero>

            <CallToAction>
                <AddAnEntryCTA>
                <Link href="/add-link">
                    <Button>
                        Add a link
                    </Button>
                </Link>
                </AddAnEntryCTA>

                <Padding/>
                <Link href="/entry/Bitcoin: A Peer-to-Peer Electronic Cash System">
                    <a>See an example <i className="fas fa-arrow-right"></i></a>
                </Link>
            </CallToAction>
        </HeroBlock>

        <Blocks>
            <Block>
                <h2>Uncensorable</h2>
                <p>
                    Entries are stored on the <a href="http://ethereum.org/">Ethereum</a> blockchain. Data is hosted in the <a href="https://ipfs.io/">IPFS</a> cloud, 🧲 BitTorrent, you name it. The domain is hosted on <a href="https://ens.domains/">ENS</a>. P2P SciHub, anyone?
                </p>
            </Block>

            <Block>
                <h2>High Quality</h2>
                <p>
                    No adlinks, no captchas. The first decentralised registry to be curated with <a href="https://medium.com/giveth/conviction-voting-a-novel-continuous-decision-making-alternative-to-governance-aa746cfb9475">conviction</a>. Like Reddit for pirates.
                </p>
            </Block>

            <Block>
                <h2>A Common resource, forever.</h2>
                <p>
                    Literally anyone (or anything) can contribute. Data is never deleted, and is openly accessible to anyone to build, analyse and share. 
                </p>
            </Block>

        </Blocks>

        <FooterCtn>
        <Footer>
            Built with 🧨 by <a href="https://twitter.com/liamzebedee">@liamzebedee</a> &middot; <a href="https://github.com/liamzebedee/retrust">github</a> &middot; <a href="https://etherscan.io/address/0x201DF8201D9d0DB92A45A21A50E4fcbB00b18839">shout some eth</a>
        </Footer>
        </FooterCtn>
        

        {/* <h2>Newest entries</h2>
        <ul>
            {misc.newestEntries.map(title => {
                return <li>
                    <Link key={title} href={`/entry/${title}`}>
                        <a>{title}</a>
                    </Link>
                </li>
            })}
        </ul> */}
        
    </PageTemplate>
}

function mapStateToProps(state, props) {
    return state;
}

export default connect(mapStateToProps, null)(Home)