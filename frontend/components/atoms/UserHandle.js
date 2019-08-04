import React from 'react'

const UserHandle = ({ link=false, user, id }) => {
    let format = null
    if(user == null) {
        format = '#'+id
    } else {
        format = '@'+user.username
    }

    if(user) {
        return <a href={`/user/${user.username}`}>
            {format}
        </a>
    } else {
        return <a href={`/user/?id=${id}`}>
            {format}
        </a>
    }
}


export { UserHandle }