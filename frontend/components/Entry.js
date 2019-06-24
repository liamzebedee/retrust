import { connect } from "react-redux";
import Results from './Results'

import styled from 'styled-components';

const Title = styled.h3`
    font-size: 22px;
`

const EntryStyle = styled.div`
    margin: 1em 2em;
`

const SmallText = styled.div`
    font-size: 11px;
    margin-bottom: 1em;
`

function Entry({ title, results }) {
    return <EntryStyle>
        <SmallText>search results for:</SmallText>
        <Title>{title}</Title>
        <Results results={results}/>
    </EntryStyle>
}

export default connect()(Entry)