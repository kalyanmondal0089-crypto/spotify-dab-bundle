#creating streaming table
import dlt

@dlt.table(
    name='first_streaming_table'
)
def first_streaming_table():
    df=spark.readStream.table('spotify_cata.silver.dimuser')
    return df

#create materialized view
@dlt.table(
    name='first_mat_view'
)
def first_mat_view():
    df=spark.read.table('spotify_cata.silver.dimuser')
    return df

#create batch view
@dlt.view(
    name='first_batch_view'
)
def first_batch_view():
    df=spark.read.table('spotify_cata.silver.dimuser')
    return df

#create streaming view
@dlt.view(
    name='first_stream_view'
)
def first_stream_view():
    df=spark.readStream.table('spotify_cata.silver.dimuser')
    return df