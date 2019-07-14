import React, { useState } from "react";
import { search } from "../actions";
import { connect } from 'react-redux'

import styled from 'styled-components';
const UserProfileBox = styled.input``

const Style = styled.div`
    flex: 1;
    align-self: center;
`

const UserProfile = ({ dispatch, user }) => {
    return <Style>
        <a href={`/user/${user.username}`}>{user.username}</a> ({user.reputation})
    </Style>
}

function mapStateToProps(state) {
    return state;
}

export default connect(mapStateToProps)(UserProfile)