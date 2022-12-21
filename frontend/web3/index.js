import Web3 from 'web3'

// const web3 = new Web3('http://localhost:8545' , null, { });
// || Web3.givenProvider

// Metamask automatically does gas estimation for us
const web3 = new Web3(window.ethereum);

export { web3 }