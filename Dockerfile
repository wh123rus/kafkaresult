# 기본 이미지 설정
FROM python:3.8-alpine

# 작업 디렉토리 설정
WORKDIR /app

# .dockerignore에서 제외된 디렉토리 이외의 모든 파일을 복사
COPY . /app/

# 필요한 패키지 설치 (Alpine 리눅스에서는 필요한 패키지를 apk를 통해 설치합니다)
RUN apk update && apk add --no-cache \
    gcc musl-dev mariadb-connector-c-dev mariadb-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir \
    && apk del --rdepends --purge musl-dev gcc \
    && chmod +x /app/cmd.sh

# 컨테이너 실행 시 자동으로 실행될 명령어 설정
USER 1001
