import dlt

#ingesting products

product_rules={
    'rule1':'product_id is not null',
    'rule2':'price >=0'
}
@dlt.expect_all_or_drop(product_rules)
@dlt.table(
    name='product_stg'
)
def product_stg():
    df=spark.readStream.table('spotify_cata.bronze.products')
    return df