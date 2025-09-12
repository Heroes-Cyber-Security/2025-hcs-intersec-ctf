FROM python:3.12-slim

WORKDIR /app

COPY src/requirements.txt .

RUN apt-get update && apt-get install -y \
    socat \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

COPY src/ .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 1337

CMD ["/entrypoint.sh"]
