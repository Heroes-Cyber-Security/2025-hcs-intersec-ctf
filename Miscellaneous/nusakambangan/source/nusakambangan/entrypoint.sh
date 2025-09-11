#!/bin/sh

FLAG_INIT="HCS{Jail_j4il_j4il_nUsakamb4ngan!!!_[UUID]}"
FLAG=${FLAG_INIT//'[UUID]'/$FLAG}

echo $FLAG > /app/flag.txt

unset FLAG_INIT
unset FLAG

rm -rf /entrypoint.sh

exec socat TCP-LISTEN:1337,reuseaddr,fork EXEC:/app/app.py