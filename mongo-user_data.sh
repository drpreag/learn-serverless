#!/bin/bash
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
apt-get update
apt-get install -y mongodb-org  --allow-unauthenticated
systemctl daemon-reload
systemctl start mongod
systemctl enable mongod
apt-get upgrade -y
apt install mongodb-clients

export LC_ALL=C
mongo
# within mongo client run:
use admin
db.createUser({user:"admin", pwd:"*******", roles:[{role:"root", db:"admin"}]})