from sqlalchemy import Integer, Column
from database import Base


class Bar(Base):
    __tablename__ = "bars"

    id = Column(Integer, primary_key=True)