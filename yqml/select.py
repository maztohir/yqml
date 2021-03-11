from yqml.keys import Keys
from .where import Where
from .join import Join, RightJoin, LeftJoin
from .fields import Fields

class Select:
    def __init__(self, dict):
        self._content = dict

    def to_sql(self):
        query = f"SELECT {self.field_clause} {self.from_clause} {self.join_clause} {self.left_join_clause} {self.right_join_clause} {self.where_clause}"
        return query
    
    @property
    def field_clause(self):
        return Fields(self._content.get(Keys.SELECT)).to_raw_sql()
    
    @property
    def from_clause(self):
        return From(self._content).to_raw_sql()
    
    @property
    def join_clause(self):
        return Join(self._content).to_raw_sql()

    @property
    def right_join_clause(self):
        return RightJoin(self._content).to_raw_sql()

    @property
    def left_join_clause(self):
        return LeftJoin(self._content).to_raw_sql()

    @property
    def where_clause(self):
        return Where(self._content).to_raw_sql()

class From:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        table_id = self._content.get(Keys.FROM)
        return f'FROM {table_id}'