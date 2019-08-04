#!/bin/bash
set -ex
source ./seth.env

make all

LOG=./deploy/LOG

export REGISTRY=$(seth send --create $(cat ./out/Registry.bin) --status 2>/dev/null)
echo -n $REGISTRY > ./deploy/Registry

export GUACTOKEN=$(seth send --create $(cat ./out/GUACToken.bin) --status 2>/dev/null)
echo -n $GUACTOKEN > ./deploy/GUACToken

export MEMBERNFT=$(seth send --create $(cat ./out/MemberNFT.bin) "MemberNFT(address)" $GUACTOKEN --status 2>$LOG)
echo -n $MEMBERNFT > ./deploy/MemberNFT

seth send $GUACTOKEN "setup(address)" $MEMBERNFT --status 2>$LOG


tee ./deploy/deployments.env.sh << EOF
export REGISTRY=$REGISTRY
export GUACTOKEN=$GUACTOKEN
export MEMBERNFT=$MEMBERNFT
EOF

echo 'Success'