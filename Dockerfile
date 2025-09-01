# Use the official NGINX Alpine image
FROM nginx:alpine

# Copy your index.html to the default nginx directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 6666
EXPOSE 6666

# Change the default port from 80 to 6666 and start nginx
CMD ["/bin/sh", "-c", "sed -i 's/listen       80;/listen       6666;/' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
