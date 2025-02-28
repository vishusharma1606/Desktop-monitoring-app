# Use an appropriate base image
FROM python:3.13.2

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8081

CMD ["python3", "server.py"]