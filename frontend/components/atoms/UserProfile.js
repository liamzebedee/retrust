import React, { useState } from "react";
import { search } from "../../actions"
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import Button from '../Button'
import Link from 'next/link'

import styled from 'styled-components';
import UserSelector from "./UserSelector";
const UserProfileBox = styled.input``

const Style = styled.div`
    flex: 1;
    align-self: center;
`

class UserProfile extends React.Component {
    componentDidMount() {
        this.props.loadUser()
    }

    render() {
        let props = this.props
        return props.loggedIn ? <LoggedIn {...props}/> : <NotLoggedIn/>
    }
}

const NotLoggedIn = ({ usersAvailable = [] }) => {
    return <div>
        <Link href="/register">
            <Button>
                Join
            </Button>
        </Link>
        <UserSelector/>
    </div>
}

const LoggedIn = ({ user }) => {
    return <Style>
        <Link prefetch href={`/user/${user.username}`}>{user.username}</Link> ({user.reputation})
    </Style>
}

import { loggedInUser, isLoggedIn } from '../../selectors'
import { loadUser } from "../../actions/users";

function mapStateToProps(state, ownProps) {
    const loggedIn = isLoggedIn(state)
    let user
    if(loggedIn) {
        user = loggedInUser(state)
    }
    return {
        loggedIn,
        user
    }
}

function mapDispatchToProps(dispatch, ownProps) {
    return bindActionCreators(
        {
            loadUser
        },
        dispatch
    )
}

export default connect(mapStateToProps, mapDispatchToProps)(UserProfile)