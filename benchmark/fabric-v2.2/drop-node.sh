echo "sleep 100"
sleep 100
echo "stoping peer2 org1"
docker stop peer2.org1.example.com
echo "remove peer2 org1"
docker rm peer2.org1.example.com
