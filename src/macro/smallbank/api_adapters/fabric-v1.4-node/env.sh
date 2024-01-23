export CORE_PEER_LOCALMSPID=Org1MSP 
export CORE_PEER_MSPCONFIGPATH=../../fabric-v1.4/four-nodes-docker/crypto_config/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export FABRIC_CFG_PATH=../../../../../benchmark/fabric-v1.4/four-nodes-docker

CHANNEL_NAME=rpcchannel
ORDER_ADDR=172.31.12.127:7041
PEER_ADDRS=( 172.31.12.127:7051 172.31.12.127:6051 172.31.12.127:8051 172.31.12.127:9051) # Place anchor peer at head

LANGUAGE=golang
CC_SRC_PATH=../../../../../benchmark/contracts/fabric-v1.4/smallbank
CC_NAME=smallbank
CC_VERSION=v1

