
import AddLink from './AddLink'
import { connect } from 'react-redux'
import { addToRegistry } from '../actions/registry'
import { ADD_TO_REGISTRY_PROGRESS } from '../actions/registry'

function AddLinkContainer(props) {
    return <AddLink {...props} />
}

function mapStateToProps(state, props) {
    const userId = state.user.loggedInUserId
    return {
        txhash: state.registry.addToRegistry,
        userId,
    }
}

function mapDispatchToProps(dispatch, ownProps) {
    return {
        submit: (userId, title, url) => {
            dispatch(addToRegistry(userId, title, url))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(AddLinkContainer)