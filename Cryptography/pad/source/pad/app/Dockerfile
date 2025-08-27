FROM alpine:3.18

RUN apk update && \
    apk add --no-cache python3 py3-pip socat

RUN adduser -D ctf

WORKDIR /home/ctf

COPY flag.txt /home/ctf/
COPY chall.py /home/ctf/

RUN chown -R ctf:ctf /home/ctf
RUN chmod -R 555 /home/ctf

RUN pip install pycryptodome ecdsa

EXPOSE 1337
ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork,nodelay,su=ctf", "EXEC:'timeout 60 python3 /home/ctf/chall.py'"]