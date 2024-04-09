import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

stages = os.path.join(current_dir, '..', 'stages')
sys.path.append(stages)

import deploying

def run(model):
    deployer = deploying.deployer()
    app = deployer.deploy(model)

    return app