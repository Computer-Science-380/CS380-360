from sqlalchemy import create_engine
import pandas as pd

server = 'DANIELFIGUEROA'
database = 'CS360'  

engine = create_engine(f'mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

query = "SELECT * FROM WordBank" 
df = pd.read_sql(query, engine)

print(df)
