#!/bin/sh
set -eu

FLAG_INIT="HCS{how_different_was_this_from_ecb_oracle?_quite_different_huh_[UUID]}"
FLAG=${FLAG_INIT//'[UUID]'/$FLAG}

echo -n "$FLAG" > /home/ctf/flag.txt
chown ctf:ctf /home/ctf/flag.txt
chmod 400 /home/ctf/flag.txt

unset FLAG FLAG_INIT

exec socat TCP-LISTEN:1337,reuseaddr,fork,nodelay,su=ctf \
  "EXEC:'sh -lc \"cd /home/ctf && timeout 60 python3 chall.py\"'"
