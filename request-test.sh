#!/bin/bash

curl --request GET http://127.0.0.1:5000/api/timeline_post

curl -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=declan&email=dstaunton@tamu.edu&content=Testing my endpoints'

curl http://127.0.0.1:5000/api/timeline_post
