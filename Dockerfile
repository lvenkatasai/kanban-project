FROM nginx:alpine

# Copy your app
COPY index.html /usr/share/nginx/html/

# Expose port 6666
EXPOSE 6666

# Start nginx on port 6666
CMD ["sh", "-c", "sed -i 's/listen       80;/listen       6666;/' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
