from sqlalchemy import TIMESTAMP, Column
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import current_timestamp


class TimestampMixin(object):
    @declared_attr
    def created_at(cls):
        return Column(TIMESTAMP,
                      nullable        = False,
                      server_default  = current_timestamp(),
                      comment         = "作成日時")

    @declared_attr
    def updated_at(cls):
        return Column(TIMESTAMP,
                      nullable        = False,
                      server_default  = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                      comment         = "更新日時")

    @declared_attr
    def ignored_at(cls):
        return Column(TIMESTAMP,
                      nullable        = True,
                      server_default  = None,
                      comment         = "無効日時")
