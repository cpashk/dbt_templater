{%- macro render_columns(columns) -%}

{%- for i in range(columns|length) %}
  -- {{ columns['column_name'][loop.index0] }}
  {%- if not loop.last -%},{%- endif -%}
{%- endfor %}

{%- endmacro %}

with base as (

  select * from {% raw %}{{{% endraw %} source('{{ schema }}', '{{ table }}') {% raw %}}}{% endraw %}

), renaming as (

  select  {{ render_columns(columns) }}
  from base

), casting as (

  select  {{ render_columns(columns) }}
  from renaming

)

select * from casting
