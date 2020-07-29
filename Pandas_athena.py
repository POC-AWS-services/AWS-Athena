# You can use the pandas.read_sql to handle the query results as a DataFrame object.

from pyathena import connect
import pandas as pd

conn = connect(aws_access_key_id='YOUR_ACCESS_KEY_ID',
               aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
               s3_staging_dir='s3://YOUR_S3_BUCKET/path/to/',
               region_name='us-west-2')
df = pd.read_sql("SELECT * FROM many_rows", conn)
print(df.head())
print(df.head())