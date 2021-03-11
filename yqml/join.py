from .keys import Keys

class Join:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        table_id = self._content.get(Keys.JOIN)
        return f'JOIN {table_id}'

    
