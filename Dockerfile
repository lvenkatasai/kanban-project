FROM node:18-alpine
WORKDIR /app
COPY public/ ./public
RUN npm install -g serve
EXPOSE 6666
CMD ["serve", "-s", "public", "-l", "6666", "--no-clipboard"]
