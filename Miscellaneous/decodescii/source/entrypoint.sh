#!/bin/bash

FLAG_INIT="HCS{weird_4hhh_fl4gzz_ye_aw1kw0k_[UUID]}"
FLAG=${FLAG_INIT//'[UUID]'/$FLAG}

export USERNAME=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 8) && \
    useradd -m -s /bin/bash "$USERNAME" && \
    chown -R "$USERNAME:$USERNAME" /app

echo $FLAG > /home/$USERNAME/flag.txt
chown $USERNAME:$USERNAME /home/$USERNAME/flag.txt

unset FLAG_INIT
unset FLAG

rm -rf /entrypoint.sh

socat TCP-LISTEN:1337,reuseaddr,fork,nodelay,su=$USERNAME EXEC:"env USERNAME=$USERNAME timeout 360 python3 /app/main.py"