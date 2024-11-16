FROM python:3.11-slim

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    pkg-config \
    default-libmysqlclient-dev \
    && apt-get clean

# 작업 디렉토리 설정
WORKDIR /app

# wait-for-it.sh 복사
COPY wait-for-it.sh /wait-for-it.sh

# requirements.txt 복사 및 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 프로젝트 전체 복사
COPY todolist /app/todolist

# 컨테이너 실행 명령
CMD ["/wait-for-it.sh", "mysql:3306", "--", "python", "todolist/manage.py", "runserver", "0.0.0.0:8000"]
