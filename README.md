# YQML
### YAML based query language.

This library will help you convert a YAML into a Query script.

## Why using YAML for the query?
The query is purely text, hard to parse and convert into any form that we want. Also programming language can't read query text properly. But YAML does.


If you have a query that become a source of truth in your service, and need to be convertible or extract to every form let say `json/yaml/erd/schema/others` then this is the answer.

By using YQML, you write the Query in YAML format and it's transformable into SQL syntax.

## Advantage
- Your query will be easy to read by your programming language, since its YAML
- Your query is not isolated with Query engine (say Postgres, MySQL, Bigquery), when you're doing some migration, your query is safe.
- you can use sharing function / available yqml library around the world to get you covered, say for building SCD table, Fact accumulated, etc
- You can apply any templating/function before render into some query

## Sample

<table>
<tr>
  <th>SQL</th>
  <th>YQML</th>
</tr>
<tr>
  <td>

  ```sql
  -- simple syntax
  SELECT
    id, 
    name,
    address
  FROM 
    persons
  ```
  </td>
  <td>

  ```yaml
  select:
    - id
    - name
    - address
  from: persons
  ```

  </td>
</tr>
<tr>
  <td>

  ```sql
  -- syntax with CTE
  WITH
  raw_data AS (
  SELECT
    id, 
    name as person_name,
    left(address,10) as address
  FROM 
    persons
  WHERE
    id > 1213
  )
  SELECT
    address, 
    count(*) total_person
  FROM raw_data
  GROUP BY 1
  ```
  </td>
  <td>

  ```yaml
  with:
    raw_data:
      select:
        - name: id
        - name: person_name
          source: name
        - aname: address
          source: left(address,10)
      from: persons
      where: >
        id > 1213
    
    select: 
      - name: address
      - name: total_persons
        source: count(*)
    from: raw_data
    group_by:
      - address
  ```
  </td>
</tr>

<tr>
  <td>

  ```sql
  -- syntax with complex templating/function
  WITH
  scd_type2_raw AS (
  SELECT
    id, 
    name as person_name,
    left(address,10) as address
  FROM 
    persons
  )
  -- ..... 1000lines more here
  SELECT
    person_id, 
    person_name,
    person_address
  FROM semi_final_raw
  ```
  </td>
  <td>

  ```yaml
  function:
    - log_to_scd_type2
  
  log_to_scd_type2:
    select: 
      - name: person_id
        source: id
      - name: person_name
        source: name
      - name: person_address
        source: address
    from:
      persons
  ```
  </td>
</tr>
</table>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install yqml. 

```bash
pip install yqml
```

## Usage

```python
from yqml.yqml import YQML

import yaml

content = yaml.safe_load(file)
engine = YQML(content, engine='bigquery')

sql = engine.to_sql()
print(sql)
```

## What's supported now
- Supporting simple SQL (Select, From, Where, Join)

## TODO
- Supporting CTE
- Supporting MERGE
- Supporting Scripting
- Better to handling multiple JOIN statement
- Supporting function import / tmplating

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
