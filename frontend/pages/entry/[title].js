import React, { useState, useEffect } from "react"
import { connect } from 'react-redux'
import PageTemplate from "../../components/PageTemplate"
import EntryContainer from '../../components/EntryContainer'
import { useRouter } from 'next/router'
import { loadEntry } from '../../actions/registry'


function EntryPage({ load }) {  
    const router = useRouter()
    const { title } = router.query

    const entry = {
        title
    }

    return <PageTemplate>
        <EntryContainer {...entry}/>
    </PageTemplate>
}

function mapStateToProps(state, props) {
    return state;
}

function mapDispatchToProps(dispatch) {
    return {}
}

export default connect(mapStateToProps, mapDispatchToProps)(EntryPage)