import HomePage from '../components/HomePage'
import { connect } from 'react-redux'
import { loadNewestEntries } from '../actions/registry'

class HomePageContainer extends React.Component {
    componentDidMount() {
        this.props.load()
    }

    render() {
        return <HomePage/>
    }
}


function mapStateToProps(state, ownProps) {
    return state
}

function mapDispatchToProps(dispatch) {
    return {
        load: () => {
            dispatch(loadNewestEntries())
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(HomePageContainer)