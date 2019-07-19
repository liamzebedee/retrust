import PageTemplate from '../components/PageTemplate'
import Button from '../components/Button'
import styled from 'styled-components';
import AddLinkContainer from '../components/AddLinkContainer';
import ExpandableAddress from '../components/ExpandableAddress'

const Title = styled.h2`
    font-size: 24px;
`

const DashStyle = styled.div`
margin: 2em 3em;
`

const theFounder = '0x28EF2d65f77E2F51752776c53fC341980ED746B2'

function DashPage() {
    return <PageTemplate>
        <DashStyle>
            <Title>Your community</Title>

            <Title>FAQ</Title>
            <h4>Who moderates GUAC?</h4>
            <div>
                <p>The founder ({ExpandableAddress(theFounder)}) owns 10 000 GUAC.</p>
                <p>The job of the moderator is to grow the community. They verify contributions by users, which in turn awards reputation. </p>
                <p>Reputation is the internal currency of guac.</p>
            </div>
            <h4>How do I participate?</h4>
            <div>
                <p>To participate you need at least 100 reputation.</p>
                <p>By making a small deposit of $10 DAI, we are able to ensure anyone can join.</p>
                <p>Contributing earns you reputation. </p>
            </div>
            <h4>How does the GUAC currency work?</h4>
            <div>
                <p>If you've ever used Reddit, you know about getting reputation from making good posts.</p>
                <p>Guac is like this, but with a twist -</p>
                <p>1) since we're not just amassing memes, but <b>curating</b>, there is a slightly more objective criteria we are working towards</p>
                <p>2) those who make good content get awarded reputation</p>
                <p>3) at any point, users can cash in their reputation for DAI</p>
                <p>4) the longer you've held your reputation, the more valuable it becomes.</p>
            </div>

        </DashStyle>
    </PageTemplate>
}

export default DashPage