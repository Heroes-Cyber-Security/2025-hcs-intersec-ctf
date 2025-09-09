FROM php:8.2-apache

COPY html/ /var/www/html/
COPY flag.txt /flag.txt

RUN chmod 644 /flag.txt
RUN echo "How could you :P" > /usr/local/lib/php/pearcmd.php

EXPOSE 80
