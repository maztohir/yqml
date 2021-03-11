from .keys import Keys

class Field:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        if self.source != self.name:
            return f'{self.source} AS {self.name}'
        else:
            return self.name

    @property
    def name(self):
        return self._content.get(Keys.NAME)
    
    @property
    def source(self):
        if self._content.get(Keys.SOURCE):
            return self._content.get(Keys.SOURCE)
        else:
            return self._content.get(Keys.NAME)
    
