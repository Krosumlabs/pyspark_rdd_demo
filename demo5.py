from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("RDDExample1").master("local[*]").getOrCreate()

sc = spark.sparkContext

sales = [1000,2000,3000,4000,5000]


rdd = sc.parallelize(sales)

print(f"\n\n Check number of partition:{rdd.getNumPartitions()}")

def show_partition(index,iterator):
    return [(index ,list(iterator))]

result = rdd.mapPartitionsWithIndex(show_partition)

print(result.collect())

# P1(0) ->[1000,2000]
# P2(1) ->[3000,4000]
# P3(2) ->[5000,]


rdd = sc.parallelize(sales,3)

print(f"\n\n Check number of partition:{rdd.getNumPartitions()}")

def show_partition(index,iterator):
    return [(index ,list(iterator))]

result = rdd.mapPartitionsWithIndex(show_partition)
print(result.collect())
