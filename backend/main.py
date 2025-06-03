# import FastAPI
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Import SQLAlchemy engine, session tools, and ORM models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base, TireBrand

# read CSV
from .read_allSpecs import spec_list
from typing import List
from pydantic import BaseModel

# Pydantic 回傳模型
class Brand(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

# Dependency: 每次請求建立一個資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# ✅ 替換成你自己的 PostgreSQL 連線資訊
DATABASE_URL = "postgresql://soul:1234@localhost:5432/test"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Remix dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/specs")
def get_specs():
    return [{"id": 1, "spec": "225/55/17"}, {"id": 2, "spec": "195/65/15"}]

@app.get("/api/brand", response_model=List[Brand])
def get_brands(db: Session = Depends(get_db)):
    return db.query(TireBrand).all()

@app.get("/api/allspecs")
def read_allSpecs():
    return spec_list

# def index(request: Request, db: Session = Depends(get_db)):
#     brands = db.query(TireBrand).all()
#     return templates.TemplateResponse("form.html", {
#         "request": request,
#          "brands": brands
# })