# Basic usage and connection
from pyathena import connect

cursor = connect(aws_access_key_id='YOUR_ACCESS_KEY_ID',
                 aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
                 s3_staging_dir='s3://YOUR_S3_BUCKET/path/to/',
                 region_name='us-west-2').cursor()
cursor.execute("SELECT * FROM one_row")
print(cursor.description)
print(cursor.fetchall())