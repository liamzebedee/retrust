import styled from 'styled-components';
import { connect } from 'react-redux'

const ContributeStyle = styled.div`
    align-self: center;
`



function Contribute() {
    return <ContributeStyle>
        {/* <Button>
            Add entry
        </Button> */}
    </ContributeStyle>

}

export default connect()(Contribute)