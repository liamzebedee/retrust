import { connect } from 'react-redux'
import styled from 'styled-components'
import { useState } from 'react'

const TxTracker = styled.div`
    font-size: 12px;
    margin: 1em 0em;
`

function TxStatusWidget({ status, txhash }) {
    if(!txhash) return null

    let [expanded, setExpanded] = useState(false)

    let statusEl
    switch(status) {
        case 'processing':
            statusEl = <i class="fab fa-buffer"></i>
        case 'confirmed':
            statusEl = <i class="fas fa-check-circle"></i>
    }

    return <TxTracker>
        <span onClick={() => setExpanded(true)}>
            tx {expanded && txhash}
        </span>: {statusEl}
    </TxTracker>
}

function mapStateToProps(state, ownProps) {
    const info = state.txs[ownProps.txhash]
    return {
        ...info
    }
}

function mapDispatchToProps(dispatch, ownProps) {
    return {}
}

export default connect(mapStateToProps, mapDispatchToProps)(TxStatusWidget)