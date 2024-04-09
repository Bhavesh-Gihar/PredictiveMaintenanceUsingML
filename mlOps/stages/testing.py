import findspark
findspark.init()

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

class tester:
    def test(self, model, test_data):
        predictions = model.transform(test_data)
        evaluator = MulticlassClassificationEvaluator(labelCol="Target", predictionCol="prediction", metricName="accuracy")
        accuracy = evaluator.evaluate(predictions)

        return accuracy
