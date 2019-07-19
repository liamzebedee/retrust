#!/bin/bash


# # Connect to the local node
# export ETH_RPC_URL=http://127.0.0.1:8545

# # Disable below if not on Truffle
# export ETH_GAS=4712388

# # Use the unlocked RPC accounts
# export ETH_RPC_ACCOUNTS=yes

# # Get the 1st account and use it
# export ETH_FROM=$(seth accounts | head -n1 | awk '{ print $1 }')

source ./env.sh

# seth call $EBSL_CORE "check_xtol(uint168,uint168)(bool)" 1012329203 123981231782
# seth call $EBSL_CORE "to_opinion(int128)(uint168[3] memory)" 3

# seth call $EBSL_CORE "opinion_add(uint168[3] memory x, uint168[3] memory y)(uint168[3] memory)" "[000000000000000000000000000000000165a0bc00,000000000000000000000000000000000000000000,0000000000000000000000000000000000ee6b2800]" "[000000000000000000000000000000000165a0bc00,000000000000000000000000000000000000000000,0000000000000000000000000000000000ee6b2800]"

# seth call $EBSL "ebslConverge2()"
seth call $EBSL "ebslConverge()"

# seth call $EBSL "getOpinion(address,address)(uint168[3] memory)" $ETH_FROM $ETH_FROM

# seth send $TRUST_TOKEN "trust(address,address,int128)" $ETH_FROM $ETH_FROM 100