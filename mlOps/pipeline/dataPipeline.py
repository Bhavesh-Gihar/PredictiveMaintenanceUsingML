from stages import dataIngestion, dataCleaning, dataValidationSplit

def run():
    data = dataIngestion.data("dataset/predictive_maintenance.csv")

    dataCleaner = dataCleaning.dataCleaner()
    data.df = dataCleaner.clean(data.df)

    splitter = dataValidationSplit.dataValidationSplitter()
    training_data, testing_data = splitter.split(data, 0.9)

    return training_data, testing_data