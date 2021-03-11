from .keys import Keys

class From:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        table_id = self._content.get(Keys.FROM)
        return f'FROM {table_id}'

    
