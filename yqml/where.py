from .keys import Keys

class Where:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        table_id = self._content.get(Keys.WHERE)
        return f'WHERE {table_id}'

    
