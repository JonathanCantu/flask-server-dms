#!/bin/bash

# Assume we have psql and postgres install:
dropdb -U postgres "digital_media_store"
createdb -U postgres "digital_media_store"
psql --host=localhost --dbname=digital_media_store -U postgres -f ./digitalmediastore.sql

# Setup the virtual environment:
source ./venv/bin/activate

# Pull in the dependencies:
pip3 install -r requirements.txt

# Run the server
python3 -m swagger_server

