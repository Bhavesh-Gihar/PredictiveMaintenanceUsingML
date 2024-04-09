import findspark
findspark.init()

from pyspark.ml.feature import VectorAssembler

class dataCleaner:
    def clean(self, data):
        columns_to_drop = ["UDI", "Product ID", "Type", "Failure Type"]
        data = data.drop(*columns_to_drop)

        feature_columns = data.columns[:-1]
        assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
        data = assembler.transform(data)

        return data