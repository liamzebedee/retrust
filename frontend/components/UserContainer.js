import React, { useState, useEffect } from "react"
import { connect } from 'react-redux'
import User from './User'
import { useRouter } from 'next/router'
import { loadUser } from '../actions/users'
import { getUser } from "../selectors";
import { bindActionCreators } from "redux";

class UserContainer extends React.Component {
    componentDidMount() {
        this.props.loadUser(this.props.id)
    }

    render() {
        return this.props.user !== null ? <User {...this.props.user}/> : 'Loading'
    }
}

function mapStateToProps(state, ownProps) {
    let user = getUser(state, ownProps.id)
    return {
        user
    }
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(
        {
            loadUser
        },
        dispatch
    )
}

export default connect(mapStateToProps, mapDispatchToProps)(UserContainer)