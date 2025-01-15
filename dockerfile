FROM python:3.12.4

WORKDIR /app

# 의존성 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 필요한 Python 패키지를 설치
RUN pip install flask flask-cors

# 소스 코드 복사
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
