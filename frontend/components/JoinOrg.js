import { connect } from "react-redux";
import Results from './Results'

import styled from 'styled-components';

function Entry({ x }) {
    return <div>
        Deposit $X for $Y rep
    </div>
}

export default connect()(Entry)