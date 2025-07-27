#!/bin/bash

git fetch
git reset origin/main --hard
source .venv/bin/activate
pip install -r requirements.txt

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build