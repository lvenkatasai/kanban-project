# Kanban Simple

A simple Kanban board built with **FastAPI**, **SQLite**, and **React (via CDN)**.

## Features
- Create & delete boards
- Add, update, and drag tasks between columns (To Do, In Progress, Done)
- Import/export tasks as CSV
- REST API with FastAPI

## Requirements
- Python 3.11+
- pip

## Installation
```bash
git clone <this-repo>
cd kanban-simple
pip install -r requirements.txt
```

## Running locally
```bash
uvicorn app:app --reload
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

## Running with Docker
```bash
docker build -t kanban-simple .
docker run -p 8000:8000 kanban-simple
```

Then open [http://localhost:8000](http://localhost:8000).
