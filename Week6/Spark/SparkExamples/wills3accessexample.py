from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

load_dotenv()

spark = SparkSession.builder \
    .appName("S3Minimal") \
    .config("spark.jars.packages","org.apache.hadoop:hadoop-aws:3.4.1,com.amazonaws:aws-java-sdk-bundle:1.12.700") \
    .config("spark.sql.warehouse.dir", "s3a://willmar5/warehouse/")\
    .enableHiveSupport() \
    .getOrCreate()

hconf = spark._jsc.hadoopConfiguration()
hconf.set("fs.s3a.access.key", os.getenv("AWS_ACCESS_KEY_ID"))
hconf.set("fs.s3a.secret.key", os.getenv("AWS_SECRET_ACCESS_KEY"))

# Spark reads/writes S3 using credentials from profile or env
df = spark.createDataFrame([(1,"Alice"),(2,"Bob")], ["id","name"])

df.write.mode("overwrite").parquet("s3a://willmar5/test/")

df2 = spark.read.parquet("s3a://willmar5/test/")
df2.show()


# -------------------------------
# 2. Sample data
# -------------------------------
users_data = [
    (1, "Alice", "NY"),
    (2, "Bob", "CA"),
    (3, "Charlie", "TX"),
    (4, "Diana", "NY"),
    (5, "Eve", "CA")
]

users_df = spark.createDataFrame(users_data, ["user_id", "name", "state"])
users_df2 = spark.createDataFrame(users_data, ["user_id", "name", "state"])
# -------------------------------
# 3. Drop table if exists
# -------------------------------
spark.sql("DROP TABLE IF EXISTS users_bucketed")

# Save to S3 (partitioned by state)
users_df.write \
    .partitionBy("state") \
    .mode("overwrite") \
    .parquet("s3a://willmar5/users_bucketed/")

# -------------------------------
# 4. Create bucketed + partitioned table
# -------------------------------
spark.sql("DROP TABLE IF EXISTS users_bucketed3")
users_df2.write \
    .partitionBy("state") \
    .bucketBy(4, "user_id") \
    .sortBy("user_id") \
    .mode("overwrite") \
    .option("path", "s3a://willmar5/tables/users_bucketed3") \
    .saveAsTable("users_bucketed3")

print("Bucketed table created:")
spark.sql("DESCRIBE EXTENDED users_bucketed3").show(truncate=False)

platinum_df = spark.table("users_bucketed3")
platinum_df.show()

# # -------------------------------
# # 6. Insert a new row
# # -------------------------------
new_user = [(6, "Frank", "TX")]
#new_user = [(7, "Johhn", "TX")]
new_df = spark.createDataFrame(new_user, ["user_id", "name", "state"])

# Append to the existing bucketed table
new_df.write \
    .mode("append") \
    .format("hive") \
    .insertInto("users_bucketed3")

print("After inserting new user:")
spark.table("users_bucketed3").show()

# NOTE:
# S3 is object storage, not HDFS. So:
# bucket joins may not always be used by the optimizer
# shuffle often still occurs
# This is why many pipelines use:
# partitioning only
# Delta Lake / Iceberg

#Also,
# Production Architecture
# In real pipelines the metastore is not stored locally or in S3. Here it is stored locally. 
# Instead it is stored in a database.

# Common setups:

# Metastore	Storage
# Hive Metastore	PostgreSQL
# Hive Metastore	MySQL
# AWS Glue Catalog	AWS managed

# The metadata DB stores things like:

# table_name
# columns
# partition columns
# bucket spec
# location (s3 path)
# Option 1 (Most common with S3): AWS Glue Catalog

# If using S3 pipelines, most people use Glue as the metastore.
# Spark config:
# spark = (
#     SparkSession.builder
#     .config("spark.sql.catalogImplementation", "hive")
#     .config("hive.metastore.client.factory.class",
#             "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory")
#     .getOrCreate()
# )

# Then tables appear in:
# AWS Glue Data Catalog

#Otherwise you have to setup and configure hive, which is no longer in the curriculum