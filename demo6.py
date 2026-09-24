'''
1. Convert telecom data into RDD
2. Perform map/filter/reduce operations
'''
# 1st import pyspark modules
from pyspark.sql import SparkSession

# 2nd create spark session object
spark = SparkSession.builder.appName("Telecom_DataFrame").getOrCreate()

# 3rd Create sparkContext
sc = spark.sparkContext

# 4th Load CSV file
rdd = sc.textFile('telecom_data.csv')

# remove header
header = rdd.first()
data_rdd = rdd.filter(lambda row: row != header)

print("==== Raw RDD Data ====")
print(data_rdd.collect())

# split CSV rows
split_rdd = data_rdd.map(lambda x:x.split(","))

# filter customers with recharge >400
high_recharge = split_rdd.filter(lambda x:int(x[5]) >400)
print("====== High Recharge Customers ======")
print(high_recharge.collect())

# Extract recharge amounts
recharge_rdd = split_rdd.map(lambda x:int(x[5]))

# Calculate total recharge
total_recharge = recharge_rdd.reduce(lambda a,b: a+b)
print("===== Total Recharge ======")
print(total_recharge)
