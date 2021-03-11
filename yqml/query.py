from .keys import Keys
from .select import Select
# from .cte import Cte

class Query:

    def is_key_exist(self, key):
        return self._content.get(key) != None

    def is_key_not_exist(self, key):
        return self._content.get(key) == None

    def __init__(self, dict):
        self._content = dict

    def is_cte(self):
        return self.is_key_exist(Keys.CTE)

    def is_simple_selection(self):
        return self.is_key_not_exist(Keys.CTE) and self.is_key_exist(Keys.SELECT)
    
    def get_raw_sql(self):
        if self.is_simple_selection():
            return Select(self._content).to_sql()

        # if self.is_cte():
        #     return Cte(self._content)
    

    #TODO:
    def is_scripting(self):
        pass

    def is_merge(self):
        pass

    def is_insert(self):
        pass

    def is_update(self):
        pass

    def is_delete(self):
        pass