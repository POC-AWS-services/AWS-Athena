from urllib.parse import quote_plus  # PY2: from urllib import quote_plus
from sqlalchemy.engine import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Table, MetaData

conn_str = 'awsathena+rest://{aws_access_key_id}:{aws_secret_access_key}@athena.{region_name}.amazonaws.com:443/'\
           '{schema_name}?s3_staging_dir={s3_staging_dir}'
engine = create_engine(conn_str.format(
    aws_access_key_id=quote_plus('YOUR_ACCESS_KEY_ID'),
    aws_secret_access_key=quote_plus('YOUR_SECRET_ACCESS_KEY'),
    region_name='us-west-2',
    schema_name='default',
    s3_staging_dir=quote_plus('s3://YOUR_S3_BUCKET/path/to/')))
many_rows = Table('many_rows', MetaData(bind=engine), autoload=True)
print(select([func.count('*')], from_obj=many_rows).scalar())