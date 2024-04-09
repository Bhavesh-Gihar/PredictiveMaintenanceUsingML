import findspark
findspark.init()

from pyspark.sql import SparkSession

class data:
    def __init__(self, path):
        spark = SparkSession.builder.appName("mlModel").getOrCreate()

        self.path = path
        self.df = spark.read.csv(self.path, header=True, inferSchema=True)