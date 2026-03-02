# 1. Import necessary modules
from pyspark.sql import SparkSession

# 2. Create SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

# 3. Load data
df = spark.read.csv("data.csv", header=True)

# 4. Transform data (transformations are lazy)
result = df.filter(df.age > 21).select("name", "age")

# 5. Trigger computation (action)
result.show()

# 6. Clean up
spark.stop()