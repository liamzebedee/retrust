import { connect } from "react-redux";

import styled from 'styled-components';

const UpVoteIcon = styled.i`
    font-size: 18px;
    transition: all 150ms;
    transition-timing-function: ease-in-out;
    :hover {
        cursor: pointer;
        transform: translate(0px, -1px);
    }
`

const DownVoteIcon = styled.i`
    font-size: 18px;
    transition: all 150ms;
    transition-timing-function: ease-in-out;
    :hover {
        cursor: pointer;
        transform: translate(0px, 1px);
    }
`

const VotePane = styled.div`
    display: inline-flex;
    flex-direction: column;
    text-align: center;
    padding-right: 1em;
`

const ResultBody = styled.div`
    display: inline-flex;
    align-self: center;
    font-size: 16px;
`

const ResultStyle = styled.div`
    display: flex;
    margin: 1em 0.25em;
`

const Link = styled.span`
    color: blue;
`


const Total = styled.span``

function Results({ results }) {
    return <div>
        {results.map(Result)}
    </div>
}

function parseLink(link) {
    let parts = link.split(':')
    const protocol = parts[0]
    return <Link>
        <a href={link}><b>{protocol}</b>:{parts.slice(1).join(':')}</a>
    </Link>
}

function Result({ total, link }) {
    return <ResultStyle>

        <VotePane>
            <UpVoteIcon className="fas fa-arrow-up"/>
            <Total>{total}</Total>
            <DownVoteIcon className="fas fa-arrow-down"/>
        </VotePane>

        <ResultBody>
            {parseLink(link)}
        </ResultBody>
    </ResultStyle>
}

export default connect()(Results)