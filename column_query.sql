select
  column_name
from information_schema.columns
where
  table_name = '{{ table }}'
  and table_schema = '{{ schema }}'
order by ordinal_position
;
