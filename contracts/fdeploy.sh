#!/bin/bash
./deploy.sh

source ./deploy/deployments.env.sh
echo -n "module.exports = '$REGISTRY'" > ../frontend/chain/Registry.js
echo -n "module.exports = '$GUACTOKEN'" > ../frontend/chain/GUACToken.js
echo -n "module.exports = '$MEMBERNFT'" > ../frontend/chain/MemberNFT.js

cp ./out/GUACToken.abi ../frontend/chain/GUACToken.json
cp ./out/MemberNFT.abi ../frontend/chain/MemberNFT.json
cp ./out/Registry.abi ../frontend/chain/Registry.json