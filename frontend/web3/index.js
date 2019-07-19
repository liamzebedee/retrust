import Web3 from 'web3'

// const web3 = new Web3('http://localhost:8545' , null, { });
// || Web3.givenProvider

// Metamask automatically does gas estimation for us
// Make sure to connect to local Ganache instance at http://localhost:8545
const web3 = new Web3(Web3.givenProvider, null, {})

export { web3 }