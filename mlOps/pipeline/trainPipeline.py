from stages import training

def run(training_data):
    trainer = training.trainer()
    model = trainer.train(training_data)

    return model