import { useState } from 'react'
import styled from 'styled-components'

const Style = styled.span`

`

const Clicker = styled.span`
    font-size: 16px;
    :hover {
        cursor: pointer;
    }
`

const Addr = styled.span`
border-bottom: 1px dotted #333;
:hover {
    border-bottom: 0;
}
`


function ExpandableAddress(addr) {
    const [expanded, setExpanded] = useState(false)
    return <Style>
        <Clicker onClick={() => setExpanded(!expanded)}>{expanded ? '+' : '-'}</Clicker>&nbsp;
        <Addr>{expanded ? `${addr.substring(0,5)}...` : addr }</Addr>
    </Style>
}

export default ExpandableAddress