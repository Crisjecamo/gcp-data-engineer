from google.cloud import bigquery

client = bigquery.Client(project="level-epoch-484223-a6")

sql = """
    SELECT *
    FROM `bigquery-public-data.thelook_ecommerce.orders`
    LIMIT 100
"""

# Run a Standard SQL query using the environment's default project
df = client.query(sql).to_dataframe()

# Run a Standard SQL query with the project set explicitly
# project_id = "level-epoch-484223-a6"
df = client.query(sql).to_dataframe()

print(df.head(10))