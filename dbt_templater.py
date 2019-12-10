from jinja2 import Template
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sys import argv
import os
import pandas as pd

dotenv_loaded = load_dotenv()

column_query_path = 'column_query.sql'
base_file_template_path = 'base_file_template.sql'

connection_url = URL(drivername='redshift',
                     username=os.getenv('REDSHIFT_USER'),
                     host=os.getenv('REDSHIFT_HOST'),
                     port=os.getenv('REDSHIFT_PORT'),
                     database=os.getenv('REDSHIFT_DATABASE'))

engine = create_engine(connection_url)


def get_columns(schema, table):
    with open(column_query_path, 'r') as file_template:
        column_query_template = Template(file_template.read())

    query = column_query_template.render(schema=schema, table=table)

    connection = engine.connect()

    columns = pd.read_sql_query(query, connection)

    connection.close()

    return columns


def render_sql(schema, table):
    with open(base_file_template_path, 'r') as file_template:
        template = Template(file_template.read())

    columns = get_columns(schema, table)

    return print(template.render(columns=columns, schema=schema, table=table))

def make_base_table(schema, table):
    with open(f'base_{schema}_{table}.sql', 'w') as output_file:
        output_file.write(render_sql(schema, table))


if __name__ == '__main__':
    render_sql(argv[1], argv[2])
