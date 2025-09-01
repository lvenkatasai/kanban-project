FROM python:3.11-alpine

WORKDIR /app
COPY index.html ./

EXPOSE 6666

CMD ["python", "-m", "http.server", "6666", "--bind", "0.0.0.0"]

