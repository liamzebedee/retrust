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

LOG=./deploy/LOG

export REGISTRY=$(seth send --create $(cat ./out/Registry.bin) --status 2>/dev/null)
echo -n $REGISTRY > ./deploy/Registry

export GUACTOKEN=$(seth send --create $(cat ./out/GUACToken.bin) --status 2>/dev/null)
echo -n $GUACTOKEN > ./deploy/GUACToken

export MEMBERNFT=$(seth send --create $(cat ./out/MemberNFT.bin) $GUACTOKEN --status 2>$LOG)
echo -n $MEMBERNFT > ./deploy/MemberNFT

seth send $GUACTOKEN "setup(address)" $MEMBERNFT --status 2>$LOG


tee ./deploy/deployments.env.sh << EOF
export REGISTRY=$REGISTRY
export GUACTOKEN=$GUACTOKEN
export MEMBERNFT=$MEMBERNFT
EOF

echo 'Success'