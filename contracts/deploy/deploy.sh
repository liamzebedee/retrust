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




seth send --create $(cat ./vyper/ebsl.bytecode)

seth send --create $(cat ./out/TrustToken.bin)

export EBSL_CORE=0x2ac80994c6ea3dc546d5ad35aba1d60bb66290ce
export TRUST_TOKEN=0x8de58e2b82e23079a83a6af60e41b8727ed3f34b


seth send --create $(cat ./out/EBSL.bin) "EBSLCore(address,address)" $EBSL_CORE $TRUST_TOKEN
export EBSL=0x1153f042bc629e1929e7e085c71f8ee0db28b0bb


seth call $EBSL_CORE "check_xtol(uint168,uint168)(bool)" 1012329203 123981231782
seth call $EBSL_CORE "to_opinion(int128)(uint168[3] memory)" 3
