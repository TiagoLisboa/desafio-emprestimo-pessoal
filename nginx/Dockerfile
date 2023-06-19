FROM nginx:1.19.0-alpine

COPY nginx-entrypoint.sh /usr/local/bin/nginx-entrypoint.sh

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

RUN ["chmod", "+x", "/usr/local/bin/nginx-entrypoint.sh"]
ENTRYPOINT ["/usr/local/bin/nginx-entrypoint.sh"]
