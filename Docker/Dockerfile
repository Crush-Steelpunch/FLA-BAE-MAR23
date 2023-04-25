FROM ubuntu
ENV CONFIG_FILE=/etc/nginx/nginx.conf
RUN apt update && apt install -y nginx
COPY index.html /var/www/html/index.html
COPY nginx2.conf /etc/nginx/
#CMD /sbin/nginx -g 'daemon off;'
ENTRYPOINT /sbin/nginx -c $CONFIG_FILE -g 'daemon off;' 