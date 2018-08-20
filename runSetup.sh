#!/bin/bash 
docker-compose up --build --force-recreate -d 
sleep 10 
docker exec miniwebproject_mongo_1 mongo admin -u root -p 123456 --eval 'db = db.getSiblingDB("mydb"); db.createUser({ user: "mini", pwd: "654321", roles: [ { role: "readWrite", db: "mydb" }] });'
