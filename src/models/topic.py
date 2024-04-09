from database import Base
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from .timestamp_mixin import TimestampMixin


class Topic(Base, TimestampMixin):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    topic = Column(Text, nullable=False, comment="トピック")

    code_step = relationship("CodeStep")

    def __init__(self, topic):
        self.topic = topic
