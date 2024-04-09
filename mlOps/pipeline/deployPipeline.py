import sys
sys.path.append('/mlOps/stages')

import deploying

def run(model):
    deployer = deploying.deployer()
    app = deployer.deploy(model)

    return app