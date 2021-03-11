
from yqml import YQML

yaml_engine = YQML('yaml_content', engine='bigquery')

yaml_engine.to_sql()