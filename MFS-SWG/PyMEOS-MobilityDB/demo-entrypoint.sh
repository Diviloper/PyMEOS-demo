#!/bin/bash
set -e

export PGPASSWORD='docker'

psql -h pymeos-demo-db -p 5432 -U docker -d mobilitydb -c "DROP DATABASE IF EXISTS demo;"
psql -h pymeos-demo-db -p 5432 -U docker -d mobilitydb -c "CREATE DATABASE demo;"
psql -h pymeos-demo-db -p 5432 -U docker -d demo -c "CREATE EXTENSION MobilityDB CASCADE;"
psql -h pymeos-demo-db -p 5432 -U docker -d demo -c "CREATE TABLE Trips(vehicle INTEGER,day DATE,seq INTEGER,trip tgeompoint);"

python3 /pymeos-demo/load_db.py
rm /pymeos-demo/trips.csv
rm /pymeos-demo/load_db.py

cd /pymeos-demo
jupyter notebook --allow-root --ip=0.0.0.0