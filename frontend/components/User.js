import { connect } from "react-redux";
import Results from './Results'
import React, { useState, useEffect } from "react"

import styled from 'styled-components';

const UserStyle = styled.div`
    margin: 2em 3em;
`


function User({ id, username, reputation, registered, posts, votes }) {
    return <UserStyle>
        <h2>User: {username}</h2>
        <h3>Reputation: {reputation}</h3>
        <small>Registered {""+registered}, user #{id}</small>
        <h2>Posts</h2>
        <ul>
            {posts.map(post => {
                return <li>{post}</li>
            })}
        </ul>
        <h2>Votes</h2>
        <ul>
            {votes.map(votes => {
                return <li>{vote}</li>
            })}
        </ul>
    </UserStyle>
}

export default User