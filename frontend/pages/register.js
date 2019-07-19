import PageTemplate from '../components/PageTemplate'
import Button from '../components/Button'
import styled from 'styled-components';
import AddLinkContainer from '../components/AddLinkContainer';
import ExpandableAddress from '../components/ExpandableAddress'

const Title = styled.h2`
    font-size: 24px;
`

const Style = styled.div`
margin: 2em 3em;
`

const theFounder = '0x28EF2d65f77E2F51752776c53fC341980ED746B2'

function Register() {
    return <PageTemplate>
        <Style>
            <Title>Register</Title>
            <div>
                <p>Welcome to an experiment</p>
                <p>Guac is the first openly curated index</p>
                <p>To become part of our community, you have to have a stake</p>

                <p>It's a $5 deposit to join.</p>
                <p>This price is set by the community.</p>
                <h4>What happens if I decide to leave?</h4>
                <p>Your stake will be refunded, minus the 5% commons fee.</p>
            </div>

        </Style>
    </PageTemplate>
}

export default DashPage