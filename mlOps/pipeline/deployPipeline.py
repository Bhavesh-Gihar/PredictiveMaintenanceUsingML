from stages import deploying

def run(model):
    deployer = deploying.deployer()
    app = deployer.deploy(model)

    return app