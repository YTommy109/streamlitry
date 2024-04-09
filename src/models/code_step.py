from database import Base
from sqlalchemy import Column, ForeignKey, Integer, Text

from .timestamp_mixin import TimestampMixin


class CodeStep(Base, TimestampMixin):
    """
    順序性のコード
    """
    __tablename__ = "code_steps"

    id = Column(Integer, primary_key=True)
    step = Column(Integer, nullable=False, comment="ステップ")
    code = Column(Text, comment="コード")
    topic_id = Column(Integer, ForeignKey('topic.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    def __init__(self, code: str, step: int, topic_id: int):
        self.code = code
        self.step = step
        self.topic_id = topic_id
