from main import calculate


def testCalculator():
    assert calculate("10+19") == 20
    print("It worked")


testCalculator()
