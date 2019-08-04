
import styled from 'styled-components'
import { getUsersAvailable } from '../../selectors'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import Select from 'react-select'
import { loginUser } from '../../actions/users'

const Style = styled.div`
    display: inline-block;
    width: 200px;
`

const UserSelector = ({ usersAvailable, loginUser }) => {
    return <Style>
        <Select options={usersAvailable.map(({ username, id }) => { 
            return { 
                value: id,  
                label: username
            }
        })} onChange={({ label, value }) => loginUser(value)}/>
    </Style>
}


function mapStateToProps(state, ownProps) {
    const usersAvailable = getUsersAvailable(state)
    return { usersAvailable }
}

function mapDispatchToProps(dispatch, ownProps) {
    return bindActionCreators(
        {
            loginUser
        },
        dispatch
    )
}

export default connect(mapStateToProps, mapDispatchToProps)(UserSelector)