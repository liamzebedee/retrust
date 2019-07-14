import React, { useState, useEffect } from "react"
import { connect } from 'react-redux'
import User from './User'
import { useRouter } from 'next/router'
import { loadUser } from '../actions/users'

class UserContainer extends React.Component {
    componentDidMount() {
        const { load, id } = this.props
        load(id)
    }

    render() {
        return <User {...this.props}/>
    }
}

function mapStateToProps(state, ownProps) {
    const user = state.users[ownProps.id]
    
    return {
        reputation: 1,
        registered: null,
        posts: [],
        votes: [],
        ...user,
        id: ownProps.id,
    }
}

function mapDispatchToProps(dispatch) {
    return {
        load: (id) => {
            dispatch(loadUser(id))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(UserContainer)