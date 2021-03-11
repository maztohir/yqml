
from yqml.yqml import YQML
from yqml.file import File

content = File('sample/test.yaml').yaml_dict
engine = YQML(content, engine='bigquery')

sql = engine.to_sql()
print(sql)