from .query import Query


class YQML:
    def __init__(self, raw_yaml, engine='bigquery'):
        self._raw_yaml = raw_yaml
        self._engine = engine

    def to_sql(self):
        return Query(self._raw_yaml).get_raw_sql()
        