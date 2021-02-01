import csv
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df=pd.read_csv(r"C:\Users\vinod\Desktop\Dr.KP Chandra unique lab test names_fuzzy.csv")
print(df.shape,'vinod' )
# conn=psycopg2.connect(database='v_db',user='postgres',password='vinod',host='127.0.0.1',port='5432')
# conn.autocommit = True
# cur = conn.cursor()

# df.to_sql('public.after_lockdown',con=conn, if_exists='append')

db_connection_url = "postgresql://{}:{}@{}:{}/{}".format(
    'postgres','vinod','127.0.0.1','5432','v_db')

engine = create_engine(db_connection_url)

df.to_sql('after_lockdown',engine, if_exists='append',index=False)


# df=pd.read_sql_query('select * from after_lockdown',con=conn)
# print(df)