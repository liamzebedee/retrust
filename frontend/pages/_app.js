import Head from 'next/head'
import App, { Container } from 'next/app'
import React from 'react'
import withReduxStore from '../lib/with-redux-store'
import { Provider } from 'react-redux'

import styled from 'styled-components'

const ContainerStyled = styled.div`
`



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
                 
                body {
                    font-family: "Helvetica Neue", sans-serif;
                    font-size: 14px;
                    margin: 0;
                    padding: 0;
                }
            `}</style>
          <ContainerStyled>
        <Provider store={reduxStore}>
          <Component {...pageProps} />
        </Provider>
        </ContainerStyled>
      </Container>
    </div>
  }
}

export default withReduxStore(MyApp)
