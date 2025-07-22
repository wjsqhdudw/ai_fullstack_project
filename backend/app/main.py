from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from commons.vector import connect_milvus
from commons.config import POSTGRES_URL
from commons.logger import get_logger


logger = get_logger("backend-main")

app = FastAPI()

# CORS (프론트 연동)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Milvus, DB 등 공통 커넥션 / 초기화
try : 
    connect_milvus()
    logger.info("Milvus 커넥션 성공!")
    logger.info(f"Postgres 연결 정보 : {POSTGRES_URL}")
except Exception as e :
    logger.error("초기 커넥션 실패!", exc_info=True)


# Healthchek 엔드포인트
@app.get("/health")
def health() :
    logger.info("Healthchek 요청")
    return {"status" : "ok"}

# 서버 시작 / 종료 이벤트
@app.on_event("startup")
def startup_event() :
    logger.info("서버 시작!")

@app.on_event("shutdown")
def shutdown_event() :
    logger.info("서버 종료")

@app.get("/")
def read_root() :
    logger.info("루트 API 호출")
    return {"message" : "RAG 실전 프로젝트 준비 완료!"}