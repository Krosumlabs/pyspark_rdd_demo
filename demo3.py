from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("RDDExample1").master("local[*]").getOrCreate()

sc = spark.sparkContext

sales = [1000,2000,3000,4000,5000]


rdd = sc.parallelize(sales)

total = rdd.reduce(lambda a,b:a+b)
print(total)
