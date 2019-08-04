import React, { useState, useEffect } from "react"
import { connect } from 'react-redux'
import User from './User'
import { useRouter } from 'next/router'
import { loadUser, loadUserForUsername } from '../actions/users'
import { getUser } from "../selectors";
import { bindActionCreators } from "redux";

class UserContainer extends React.Component {
    componentDidMount() {
        this.props.loadUserForUsername(this.props.username)
    }

    render() {
        return this.props.user !== null ? <User {...this.props.user}/> : 'Loading'
    }
}

function mapStateToProps(state, ownProps) {
    let user = getUser(state, ownProps.username)
    return {
        user
    }
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(
        {
            loadUserForUsername
        },
        dispatch
    )
}

export default connect(mapStateToProps, mapDispatchToProps)(UserContainer)