# Use official Node.js LTS alpine image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy your index.html file
COPY index.html ./

# Install serve package globally for static file serving
RUN npm install -g serve

# Expose port 6666
EXPOSE 6666

# Start the server on port 6666
CMD ["serve", "-s", ".", "-l", "6666", "--no-clipboard"]
