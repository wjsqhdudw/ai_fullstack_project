#!/bin/bash

docker start $(docker ps -aq)

sleep 1 

echo ""
echo "[컨테이너 기동 상태 체크]"

SERVICES=("postgres_local" "milvus-standalone")

for SERVICE in "${SERVICES[@]}"
do
    STATUS=$(docker inspect -f '{{.State.Running}}' $SERVICE 2>/dev/null)
    if [ "$STATUS" == "true" ]; then
        echo "$SERVICE: 정상 구동 중"
    else
        echo "$SERVICE: 비정상 (미실행 또는 없음)"
    fi
done

