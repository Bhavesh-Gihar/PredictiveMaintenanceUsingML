import sys
sys.path.append('/mlOps/pipeline/')

import dataPipeline, trainPipeline, testPipeline

def ciPipeline():
    training_data, test_data = dataPipeline.run()

    model = trainPipeline.run(training_data)

    accuracy = testPipeline.run(model, test_data)

    return accuracy

