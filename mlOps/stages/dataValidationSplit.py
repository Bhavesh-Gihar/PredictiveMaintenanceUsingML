class dataValidationSplitter:
    def split(self, data, k):
        (training_data, test_data) = data.df.randomSplit([k, 1-k])

        return training_data, test_data