from sqlalchemy import create_engine
import os
import clickhouse_connect
import psycopg2 as ps

connection_to = 'postgresql://{}:{}@{}:{}/{}'.format(
    'mart_sv',  # os.environ.get('USER_MART'),
    os.environ.get('PWD_MART'),
    os.environ.get('HOST_MART'),
    os.environ.get(''),
    os.environ.get('DB_MART')
)
engine_to = create_engine(connection_to)
# test = pd.read_sql('''
# select *
# from comm.gfk_from_excel
# limit 100
# ''', engine_to)
