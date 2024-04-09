import sys
sys.path.append('/mlOps/stages')

import training

def run(training_data):
    trainer = training.trainer()
    model = trainer.train(training_data)

    return model