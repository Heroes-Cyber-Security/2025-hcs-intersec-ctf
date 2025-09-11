FROM python:alpine

RUN apk add --no-cache socat

WORKDIR /app

COPY ./src/ /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 1337

CMD ["/entrypoint.sh"]