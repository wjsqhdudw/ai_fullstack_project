# 1. 공식 Python 이미지 사용
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사 및 패키지 설치
ENV PYTHONPATH=/app:/app/commons:$PYTHONPATH

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. 앱 코드 복사
COPY backend/app ./app
COPY commons ./commons

# 5. 기본 실행 명려어
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]