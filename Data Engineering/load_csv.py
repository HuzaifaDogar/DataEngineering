import pandas as pd
from sqlalchemy import create_engine

# Absolute path (IMPORTANT)
file_path = r"D:\Data Engineering\employees.xlsx"

df = pd.read_excel(file_path)

print("Data Preview:")
print(df)

engine = create_engine(
    "postgresql+psycopg2://admin:admin123@127.0.0.1:5432/companydb"
)

df.to_sql(
    "employees",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into PostgreSQL!")