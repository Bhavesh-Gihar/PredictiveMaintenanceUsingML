from pipeline import dataPipeline, trainPipeline, testPipeline, deployPipeline

training_data, test_data = dataPipeline.run()

model = trainPipeline.run(training_data)

accuracy = testPipeline.run(model, test_data)

if(accuracy > 0.5):
    app = deployPipeline.run(model)
    app.run(debug=True, port=8001, host='0.0.0.0')
else:
    print("Model failed quality check !")
