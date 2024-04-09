import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

stages = os.path.join(current_dir, '..', 'stages')
sys.path.append(stages)

import testing

def run(model, test_data):
    tester = testing.tester()
    accuracy = tester.test(model, test_data)

    return accuracy