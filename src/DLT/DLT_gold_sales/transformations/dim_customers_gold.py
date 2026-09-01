import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.view(
    name='customer_stg_view'
)
def customer_stg_view():
    df=spark.readStream.table('spotify_cata.bronze.customer_stg')
    return df.withColumn('customer_name', upper(col('customer_name')))

dlt.create_streaming_table(
    name='dim_customers'
)

dlt.create_auto_cdc_flow(
    target='dim_customers',
    source='customer_stg_view',
    keys=['customer_id'],
    sequence_by='last_updated',
    stored_as_scd_type=2
)
