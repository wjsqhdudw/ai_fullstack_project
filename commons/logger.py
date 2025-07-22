import logging
import os

def get_logger(name, log_dir="logs", level=logging.INFO) :
    """
    파일 용량 제한(순환), 포맷 일관화 패턴
    """
    if not os.path.exists(log_dir) :
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 로그 포맷 : 시간, 로그레벨, 서비스명, 메세지
    formatter = logging.Formatter(
        "[%(asctime)s][%(levelname)s][%(name)s] %(message)s", defaults="%Y-%m-%d %H:%M:%S"
    )

    # 콘솔에도 동시에 출력 (실시간 디버깅/운영 모니터링)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # 중복핸들러 방지
    logger.propagate = False

    return logger