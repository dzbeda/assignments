FROM nginx
RUN apt-get update && apt-get upgrade -y
RUN apt-get install nodejs -y
COPY index.html /usr/share/nginx/html
RUN chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid
