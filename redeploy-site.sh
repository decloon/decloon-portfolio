#!/bin/bash

tmux kill-server
git fetch
git reset origin/main --hard
source .venv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s my_server
tmux send-keys -t my_server "source .venv/bin/activate" C-m
tmux send-keys -t my_server "flask run --host=0.0.0.0" C-m