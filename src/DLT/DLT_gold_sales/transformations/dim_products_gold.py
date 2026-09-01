import dlt

from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.view(
    name='product_stg_view'
)
def product_stg_view():
    df=spark.readStream.table('spotify_cata.bronze.product_stg')
    return df.withColumn('price', col('price').cast(IntegerType()))

#create empty streaming table

dlt.create_streaming_table(
    name='dim_products'
)

dlt.create_auto_cdc_flow(
    target='dim_products',
    source='product_stg_view',
    keys=['product_id'],
    sequence_by='last_updated',
    stored_as_scd_type=2
)