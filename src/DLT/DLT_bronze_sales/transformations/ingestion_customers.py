import dlt
#expectations customer
customer_rules={
    'rule1':'customer_id is not null',
    'rule2':'customer_name is not null'
}
#ingesting products

@dlt.table(
    name='customer_stg'
)
@dlt.expect_all_or_drop(customer_rules)
def customer_stg():
    df=spark.readStream.table('spotify_cata.bronze.customers')
    return df