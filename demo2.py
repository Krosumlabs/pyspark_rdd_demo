from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("RDDExample1").master("local[*]").getOrCreate()

sc = spark.sparkContext

data = ["Python Spark","Python RDD","Spark Python"]

# flatMap()

rdd = sc.parallelize(data)

words = rdd.flatMap(lambda line:line.split(" "))
print(words.collect())
