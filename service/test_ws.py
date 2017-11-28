import unittest

if __name__ == '__main__':
    testmodules = [
        'tests.test_classification',
        'tests.test_exhibit',
        'tests.test_habitat',
        'tests.test_region',
        'tests.test_region',
        'tests.test_reset',
        'tests.test_species',
        'tests.test_state',
        'tests.test_status',
        'tests.test_zoo'
    ]

    suite = unittest.TestSuite()

    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # Else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner().run(suite)
