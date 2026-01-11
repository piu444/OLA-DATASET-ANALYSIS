import pandas as pd
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine(
    "mysql+mysqlconnector://root:@localhost/ola"
)

def run_query(query):
    """
    Executes a SQL query and returns result as a DataFrame
    """
    return pd.read_sql_query(query, engine)







