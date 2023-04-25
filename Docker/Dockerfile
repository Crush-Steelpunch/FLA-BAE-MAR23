FROM ubuntu
RUN apt update && apt install -y nginx
COPY index.html /var/www/html/index.html
#CMD /sbin/nginx -g 'daemon off;'
ENTRYPOINT /sbin/nginx -g 'daemon off;'