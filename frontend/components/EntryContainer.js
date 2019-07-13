import React, { useState, useEffect } from "react"
import { connect } from 'react-redux'
import Entry from './Entry'
import { useRouter } from 'next/router'
import { loadEntry } from '../actions/registry'

class EntryContainer extends React.Component {
    componentDidMount() {
        const { load, title } = this.props
        load(title)
    }

    render() {
        return <Entry title={this.props.title} {...this.props}/>
    }
}

function mapStateToProps(state, ownProps) {
    return {
        ...state.entry,
        title: ownProps.title,
    }
}

function mapDispatchToProps(dispatch) {
    return {
        load: (title) => {
            dispatch(loadEntry(title))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(EntryContainer)