import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

c_dir = os.path.join(current_dir, '..', 'stages')
sys.path.append(c_dir)

import training

def run(training_data):
    trainer = training.trainer()
    model = trainer.train(training_data)

    return model