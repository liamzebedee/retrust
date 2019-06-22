#!/bin/bash
set -ex

# Connect to the local node
export ETH_RPC_URL=http://127.0.0.1:8545

# Disable below if not on Truffle
export ETH_GAS=4712388

# Use the unlocked RPC accounts
export ETH_RPC_ACCOUNTS=yes

# Get the 1st account and use it
export ETH_FROM=$(seth accounts | head -n1 | awk '{ print $1 }')




export EBSL_CORE=$(seth send --create $(cat ../vyper/ebsl.bytecode) --status 2>/dev/null)
echo -n $EBSL_CORE > EBSLCore



export TRUST_TOKEN=$(seth send --create $(cat ../out/TrustToken.bin) --status 2>/dev/null)
echo -n $TRUST_TOKEN > TrustToken



export EBSL=$(seth send --create $(cat ../out/EBSL.bin) "EBSLCore(address,address)" $EBSL_CORE $TRUST_TOKEN --status 2>/dev/null)
echo -n $EBSL > EBSL