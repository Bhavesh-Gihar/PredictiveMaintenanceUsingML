import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

stages = os.path.join(current_dir, '..', 'stages')
sys.path.append(stages)

import training

def run(training_data):
    trainer = training.trainer()
    model = trainer.train(training_data)

    return model