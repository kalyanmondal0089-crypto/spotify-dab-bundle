import dlt

sales_rules={'rule1':'sales_id is not null' }

#empty streaming table
dlt.create_streaming_table(
    name='sales_stg',
    expect_all_or_drop=sales_rules
)




#creating east stream flow
@dlt.append_flow(target='sales_stg')
def east_sales():
    df=spark.readStream.table("spotify_cata.bronze.sales_east")
    return df

#creating west stream flow
@dlt.append_flow(target='sales_stg')
def west_sales():
    df=spark.readStream.table("spotify_cata.bronze.sales_west")
    return df

