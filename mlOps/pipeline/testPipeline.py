from stages import testing

def run(model, test_data):
    tester = testing.tester()
    accuracy = tester.test(model, test_data)

    return accuracy