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



export REGISTRY=$(seth send --create $(cat ../out/Registry.bin) --status 2>/dev/null)
echo -n $REGISTRY > Registry
echo -n "module.exports = '$REGISTRY'" > Registry.js

export GUACTOKEN=$(seth send --create $(cat ../out/GUACToken.bin) --status 2>/dev/null)
echo -n $GUACTOKEN > GUACToken
echo -n "module.exports = '$GUACTOKEN'" > GUACToken.js

export MEMBERNFT=$(seth send --create $(cat ../out/MemberNFT.bin) "(address)" $GUACTOKEN --status 2>/dev/null)
echo -n $MEMBERNFT > MemberNFT
echo -n "module.exports = '$MEMBERNFT'" > MemberNFT.js

seth send $GUACTOKEN "setup(address)()" $MEMBERNFT --status 2>/dev/null