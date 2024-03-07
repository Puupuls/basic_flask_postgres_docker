FROM python:3.11-alpine

WORKDIR /app
COPY . /app

RUN apk add --no-cache gcc g++ musl-dev linux-headers
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "run"]
