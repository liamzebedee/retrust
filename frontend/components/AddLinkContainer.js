
import AddLink from './AddLink'
import { connect } from 'react-redux'
import { addToRegistry } from '../actions/registry'
import { ADD_TO_REGISTRY_PROGRESS } from '../actions/registry'

function AddLinkContainer(props) {
    return <AddLink {...props} />
}

function mapStateToProps(state, props) {
    return {
        txhash: state.registry.addToRegistry
    }
}

function mapDispatchToProps(dispatch, ownProps) {
    return {
        submit: (title, url) => {
            dispatch(addToRegistry(title, url))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(AddLinkContainer)