from .keys import Keys

class Join:
    def __init__(self, dict):
        self._content = dict

    def to_raw_sql(self):
        table_id = self._content.get(self.key)
        return f'{self.phrase} {table_id}' if table_id else ''

    @property
    def key(self):
        return Keys.JOIN

    @property
    def phrase(self):
        return 'JOIN'

class RightJoin(Join):
    def __init__(self, dict):
        super().__init__(dict)

    @property
    def key(self):
        return Keys.RIGHT_JOIN

    @property
    def phrase(self):
        return 'RIGHT JOIN'

class LeftJoin(Join):
    def __init__(self, dict):
        super().__init__(dict)

    @property
    def key(self):
        return Keys.LEFT_JOIN

    @property
    def phrase(self):
        return 'LEFT JOIN'