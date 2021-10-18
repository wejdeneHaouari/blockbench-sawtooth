#!/bin/bash
sleep 1
CHANNEL_NAME=mychannel
CC_NAME=kvstore
CC_SRC_PATH="../contracts/fabric-v2.2/${CC_NAME}"
MODE=open_loop
echo "## create channel ##"
./network.sh up createChannel -ca -i 2.2 -c ${CHANNEL_NAME}
echo "## deploy cc##"
sleep 2
./network.sh deployCC -ccn ${CC_NAME} -ccp ${CC_SRC_PATH}
#echo "adding peer 2 org1"
#./addPeer.sh -o 2 -p 1 -t 8054
#sleep 2
#./deployCC.sh -t 6051 -c mychannel -d kvstore -p 1 -o 2
#sleep 2
#./addPeer.sh -o 1 -p 2 -t 7054
#sleep 2
#./deployCC.sh -t 5051 -c mychannel -d kvstore -p 2 -o 1
#sleep 2
#./addPeer.sh -o 2 -p 2 -t 8054
#sleep 2
#./deployCC.sh -t 4051 -c mychannel -d kvstore -p 2 -o 2
echo "services"
cd services
node enrollAdmin.js
sleep 2
node registerUser.js
sleep 2
node block-server.js ${CHANNEL_NAME} 8800 > block-server.log 2>&1 &
sleep 2
node txn-server.js ${CHANNEL_NAME} ${CC_NAME} ${MODE} 8801 > txn-server-8801.log 2>&1 &
