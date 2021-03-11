from .keys import Keys
from .field import Field

class Fields:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        fields = self.extract_fields()
        return ', '.join(fields)

    def extract_fields(self):
        fields = []
        for field in self._content:
            fields.append(Field(field).to_raw_sql())
        return fields
    
