import dlt
from pyspark.sql.functions import *

@dlt.view(
    name='sales_stg_trans'
)
def sales_stg_trans():
    df=spark.readStream.table('spotify_cata.bronze.sales_stg')
    return df.withColumn('total_amount', col('quantity') * col('amount'))


dlt.create_streaming_table(
    name='sales_enr'
)

dlt.create_auto_cdc_flow(
    target='sales_enr',
    source='sales_stg_trans',
    keys=['sales_id'],
    sequence_by='sale_timestamp',
    stored_as_scd_type=1
)
