sudo ./network.sh down

echo "Stop all containers"
docker stop `docker ps -qa`

echo "Remove all containers"
docker rm `docker ps -qa`

echo "Remove all volumes"
docker volume rm $(docker volume ls -q)

echo "Remove all networks"
docker network rm `docker network ls -q`
rm services/wallet/*
sudo kill $(sudo lsof -t -i:8800)
sudo kill $(sudo lsof -t -i:8801)

ps aux | grep -i block-server | awk '{print $2}' | xargs kill -9
ps aux | grep -i txn-server | awk '{print $2}' | xargs kill -9
