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

export EBSL_CORE=0x243e72b69141f6af525a9a5fd939668ee9f2b354
export TRUST_TOKEN=0x2a212f50a2a020010ea88cc33fc4c333e6a5c5c4


seth send --create $(cat ./out/EBSL.bin) "EBSLCore(address,address)" $EBSL_CORE $TRUST_TOKEN
export EBSL=0xd0828aeb00e4db6813e2f330318ef94d2bba2f60


seth call $EBSL_CORE "check_xtol(uint168,uint168)(bool)" 1012329203 123981231782
seth call $EBSL_CORE "to_opinion(int128)(uint168[3] memory)" 3

seth call $EBSL "ebslConverge2()"

seth send $TRUST_TOKEN "trust(address,address,int128)" $ETH_FROM $ETH_FROM 100