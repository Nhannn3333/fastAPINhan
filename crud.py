from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    displayname = Column(String)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Tạo kết nối đến cơ sở dữ liệu SQLite
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Tạo bảng nếu chưa tồn tại
Base.metadata.create_all(bind=engine)
