from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.expression import text
from database import Base


class CodeStep(Base):
    __tablename__ = "code_steps"

    id = Column(Integer, primary_key=True)
    step = Column(Integer, nullable=False, comment="ステップ")
    code = Column(Text, comment="コード")
    created_at = Column(TIMESTAMP, server_default=current_timestamp(), comment="作成日時")
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment="更新日時")
    ignored_at = Column(TIMESTAMP, comment="無効日時")
