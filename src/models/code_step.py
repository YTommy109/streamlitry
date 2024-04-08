from sqlalchemy import Column, Integer, Text, ForeignKey
from database import Base
from .timestamp_mixin import TimestampMixin


class CodeStep(Base, TimestampMixin):
    __tablename__ = "code_steps"

    id = Column(Integer, primary_key=True)
    step = Column(Integer, nullable=False, comment="ステップ")
    code = Column(Text, comment="コード")
    topic_id = Column(Integer, ForeignKey('topic.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
