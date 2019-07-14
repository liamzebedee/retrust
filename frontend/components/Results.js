import { connect } from "react-redux";

import styled from 'styled-components';

import moment from 'moment';

const timeAgo = (date) => {
  const now = new Date();
  const nowMoment = moment(now);
  const pastMoment = moment(date);
  const timeAgoString = pastMoment.from(nowMoment); // 2 hours ago
  return timeAgoString;
};

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
    align-self: top;
`

const ResultBody = styled.div`
    display: inline-flex;
    align-self: center;
    font-size: 16px;
    flex-direction: column;
    padding: 0 0.5rem;
`

const ResultStyle = styled.div`
    display: flex;
    margin: 1.5em 0.25em;
`

const Link = styled.span`
    color: blue;
    font-size: 18px;
    margin-bottom: 0.25em;
`


const Controls = styled.div`
    display: flex;
    font-size: 12px;
    margin-top: 0.125rem;
    font-weight: bold;
`
const SubmittedAt = styled.div`
    font-size: 12px;
    line-height: 1.2;
    color: #aaa;
`

const Meta = styled.div`
    display: flex;

    a {
        text-decoration: none;
        color: inherit;
        transition: color 50ms;
        :hover {
            color: #333;
            
        }
    }
`

const Total = styled.span``

function Results({ results }) {
    return <div>
        {results.map((result,i) => <Result key={i} {...result}/>)}
    </div>
}

function parseLink(url) {
    let parts = url.split(':')
    const protocol = parts[0]
    return <Link>
        <a href={url}><b>{protocol}</b>:{parts.slice(1).join(':')}</a>
    </Link>
}

function Result({ total, url, time, creator }) {
    if(!creator) {
        creator = "unknown"
    }
    if(!time) {
        time = "3 hours ago"
    }

    return <ResultStyle>
        <VotePane>
            <UpVoteIcon className="fas fa-arrow-up"/>
            <Total>{total}</Total>
            <DownVoteIcon className="fas fa-arrow-down"/>
        </VotePane>

        <ResultBody>
            {parseLink(url)}
            <Meta>
                <SubmittedAt>Submitted {timeAgo(time*1000)} by <a href={`/user/${creator}`}>@{creator}</a></SubmittedAt>
            </Meta>
            <Controls>
                {/* <span>flag</span> */}
            </Controls>
        </ResultBody>
    </ResultStyle>
}

export default connect()(Results)