FROM python:alpine

RUN apk add --no-cache socat
RUN pip install requests

WORKDIR /app

COPY ./src/ /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 1234

CMD ["/entrypoint.sh"]