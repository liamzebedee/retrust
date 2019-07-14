export const TX_UPDATE = 'TX_UPDATE'

export function trackTx(ev, txhash) {
    return async dispatch => {
        dispatch(txUpdate(txhash, {
            status: 'processing',
        }))

        ev.on('receipt', receipt => {
            dispatch(
                txUpdate(txhash, {
                    status: 'received',
                    receipt,
                })
            )
        })
        ev.on('confirmation', (confirmationNumber, receipt) => {
            dispatch(
                txUpdate(txhash, {
                    status: 'confirmed',
                    confirmationNumber,
                    receipt,
                })
            )
        })
        ev.on('error', err => {
            dispatch(txUpdate(txhash, {
                status: 'error',
                err
            }))
        })
    }
}

export function txUpdate(txhash, info) {
    return {
        type: TX_UPDATE,
        txhash,
        info
    }
}