from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("RDDExample1").master("local[*]").getOrCreate()

sc = spark.sparkContext

L = [1,2,3,4,5,6,7,8]

# multiply every number by 10

rdd = sc.parallelize(L)

result = rdd.map(lambda x:x * 10)
print(result.collect())
###
print("") # empty line

even_numbers = rdd.filter(lambda x: x % 2 == 0)
print(even_numbers.collect())
