import { connect } from "react-redux";

import styled from 'styled-components';

import moment from 'moment';
import { getUser } from "../selectors";
import { bindActionCreators } from "redux";
import { UserHandle } from './atoms/UserHandle'

import Result from './Result'


function Results({ results }) {
    return <div>
        {results.map((result,i) => <Result key={i} {...result}/>)}
    </div>
}



function mapStateToProps(state, ownProps) {
    return {}
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(
        {
        },
        dispatch
    )
}

export default connect(mapStateToProps, mapDispatchToProps)(Results)