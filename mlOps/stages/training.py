from pyspark.ml.classification import DecisionTreeClassifier

class trainer:
    def train(self, training_data):
        dt = DecisionTreeClassifier(labelCol="Target", featuresCol="features")
        dt_model = dt.fit(training_data)

        return dt_model
