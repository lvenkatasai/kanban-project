FROM nginx:alpine

# Create custom nginx config for port 90
RUN echo 'server { \
    listen 90; \
    server_name localhost; \
    root /usr/share/nginx/html; \
    index index.html; \
    location / { \
        try_files $uri $uri/ /index.html; \
    } \
}' > /etc/nginx/conf.d/default.conf

# Copy your HTML file
COPY index.html /usr/share/nginx/html/index.html

# Expose port 90
EXPOSE 90

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
