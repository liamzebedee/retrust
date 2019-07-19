#!/bin/bash

DIR=`pwd`
cd deploy && ./deploy1.sh

cd $DIR
cp ./deploy/GUACToken.js ../frontend/chain/GUACToken.js
cp ./deploy/MemberNFT.js ../frontend/chain/MemberNFT.js
cp ./deploy/Registry.js ../frontend/chain/Registry.js