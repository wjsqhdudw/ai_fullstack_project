#!/bin/bash

echo "=== [ 도커 전체 컨테이너 중지 ] ==="
docker stop $(docker ps -aq)

echo ""
echo "=== [ 도커 컨테이너 상태 확인 ] ==="
docker ps -a
