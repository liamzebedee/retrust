import React, { useState, useEffect } from "react"
import { connect } from 'react-redux'
import PageTemplate from "../../components/PageTemplate"
import UserContainer from '../../components/UserContainer'
import { useRouter } from 'next/router'


function UserPage({ load }) {  
    const router = useRouter()
    const { username } = router.query

    const user = {
        username
    }

    return <PageTemplate>
        <UserContainer {...user}/>
    </PageTemplate>
}

function mapStateToProps(state, props) {
    return state;
}

function mapDispatchToProps(dispatch) {
    return {}
}

export default connect(mapStateToProps, mapDispatchToProps)(UserPage)