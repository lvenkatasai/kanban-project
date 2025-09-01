# Use official Python image
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 6666

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "6666", "--reload"]
