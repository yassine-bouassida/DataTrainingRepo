from pyspark.sql import SparkSession
from pyspark.sql import Row

# -------------------------------
# 1. Start Spark session with Hive support
# -------------------------------
spark = SparkSession.builder \
    .appName("BucketingExample") \
    .config("spark.sql.warehouse.dir", "spark-warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

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

# -------------------------------
# 3. Drop table if exists
# -------------------------------
spark.sql("DROP TABLE IF EXISTS users_bucketed")

# -------------------------------
# 4. Create bucketed + partitioned table
# -------------------------------
users_df.write \
    .partitionBy("state") \
    .bucketBy(4, "user_id") \
    .sortBy("user_id") \
    .mode("overwrite") \
    .saveAsTable("users_bucketed")

print("Bucketed table created:")
spark.sql("DESCRIBE EXTENDED users_bucketed").show(truncate=False)

# -------------------------------
# 5. Query table
# -------------------------------
platinum_df = spark.table("users_bucketed")
platinum_df.show()

# -------------------------------
# 6. Insert a new row
# -------------------------------
#new_user = [(6, "Frank", "TX")]
new_user = [(7, "John", "TX")]
new_df = spark.createDataFrame(new_user, ["user_id", "name", "state"])

# Append to the existing bucketed table
new_df.write \
    .mode("append") \
    .format("hive") \
    .insertInto("users_bucketed")

print("After inserting new user:")
spark.table("users_bucketed").show()