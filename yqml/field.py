from .keys import Keys

class Field:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        if self.source:
            return f'{self.source} AS {self.field}'
        else:
            return self.field

    @property
    def field(self):
        return self._content.get(Keys.NAME)
    
    @property
    def source(self):
        if self._content.get(Keys.SOURCE):
            return self._content.get(Keys.SOURCE)
        else:
            return self._content.get(Keys.NAME)
    
