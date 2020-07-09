#!/bin/bash
set -e

# remove all the containers
docker ps -q | xargs -r docker kill
docker ps -qa | xargs -r docker rm

# remove all images
docker images -qa | xargs -r docker rmi -f
docker system prune
