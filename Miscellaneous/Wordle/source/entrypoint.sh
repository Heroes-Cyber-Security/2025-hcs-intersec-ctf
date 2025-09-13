#!/bin/sh

FLAG_INIT="HCS{u_guessed_the_word!!!_[UUID]}"
FLAG=${FLAG_INIT//'[UUID]'/$FLAG}

echo $FLAG > /app/flag.txt

unset FLAG_INIT
unset FLAG

rm -rf /entrypoint.sh

exec socat TCP-LISTEN:1234,reuseaddr,fork EXEC:/app/app.py