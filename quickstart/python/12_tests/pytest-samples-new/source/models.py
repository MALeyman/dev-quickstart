from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    created_at = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.first_name} {self.last_name}')>Y1:0"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"