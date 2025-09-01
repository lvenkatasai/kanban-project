from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.sql import func
import pandas as pd
import io
from typing import List, Dict
import os

DATABASE_URL = "sqlite:///./kanban.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    tasks = relationship("Task", back_populates="board", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    status = Column(String, default="todo")
    board_id = Column(Integer, ForeignKey("boards.id"))
    created_at = Column(DateTime, default=func.now())
    board = relationship("Board", back_populates="tasks")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kanban Board", version="1.0.0")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def parse_csv_to_tasks(csv_content: bytes) -> List[Dict]:
    try:
        df = pd.read_csv(io.BytesIO(csv_content))
        tasks = []
        for _, row in df.iterrows():
            task = {
                'title': str(row.get('title', row.iloc[0] if len(row) > 0 else 'Untitled')),
                'description': str(row.get('description', row.iloc[1] if len(row) > 1 else '')),
                'status': str(row.get('status', 'todo')).lower()
            }
            if task['status'] not in ['todo', 'in_progress', 'done']:
                task['status'] = 'todo'
            tasks.append(task)
        return tasks
    except Exception as e:
        raise ValueError(f"Error parsing CSV: {str(e)}")

def tasks_to_csv(tasks: List[Dict]) -> str:
    df = pd.DataFrame(tasks)
    return df.to_csv(index=False)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ... remaining FastAPI routes (user provided)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6666)
