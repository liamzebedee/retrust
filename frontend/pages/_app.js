import Head from 'next/head'
import App, { Container } from 'next/app'
import React from 'react'
import withReduxStore from '../lib/with-redux-store'
import { Provider } from 'react-redux'
// import { ConnectedRouter } from 'connected-react-router'
// import { history } from '../store'
// import { Switch, Route } from 'react-router'

import styled from 'styled-components'

const ContainerStyled = styled.div`
`

// import Home from './index'
// import Results from './index'


class MyApp extends App {
  render () {
    const { Component, pageProps, reduxStore } = this.props
    return <div>
        <Head>
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <meta charSet="utf-8" />
        </Head>
            
      <Container>
      <style jsx global>{`
                @import url('https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.css');
                @import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/fontawesome.min.css);
                @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.css');
                @import url('https://fonts.googleapis.com/css?family=Audiowide|Open+Sans&display=swap');

                 
                body {
                    font-family: "Helvetica Neue", 'Open Sans', sans-serif;
                    
                    font-size: 14px;
                    margin: 0;
                    padding: 0;
                }
            `}</style>
          <ContainerStyled>
            <Provider store={reduxStore}>
              {/* <ConnectedRouter history={history}> */}
                <Component {...pageProps} />
                
                {/* <>
                  <Switch>
                    <Route exact path="/" render={Home} />
                    <Route path="/results" render={Results} />
                  </Switch>
                </> */}

              {/* </ConnectedRouter> */}
            </Provider>
          </ContainerStyled>
      </Container>
    </div>
  }
}

export default withReduxStore(MyApp)
