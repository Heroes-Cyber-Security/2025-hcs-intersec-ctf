FROM php:8.2-apache
RUN a2enmod rewrite

COPY . /var/www/html/

RUN chown -R www-data:www-data /var/www/html && \
    find /var/www/html -type d -exec chmod 755 {} \; && \
    find /var/www/html -type f -exec chmod 644 {} \;

RUN echo '<Directory /var/www/html/>\nOptions -Indexes\nAllowOverride All\nRequire all granted\n</Directory>' > /etc/apache2/conf-available/app.conf \
    && a2enconf app

EXPOSE 80

ENV ACCEPT_RADIUS_M=100
