FROM alpine:3.18

RUN apk add --no-cache python3 py3-pip socat

RUN adduser -D ctf
WORKDIR /home/ctf

COPY app/ /home/ctf/
COPY entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r$//' /entrypoint.sh && \
    chmod 755 /entrypoint.sh && \
    chown -R ctf:ctf /home/ctf

RUN pip install --no-cache-dir pycryptodome ecdsa

EXPOSE 1337
ENTRYPOINT ["/entrypoint.sh"]
