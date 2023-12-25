FROM python:3.11-alpine

WORKDIR /app
copy . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "run"]
