import unittest
import sys

def runSuites(suiteList) :
	for suite in suiteList : 
		print('\n')
		print('||---- ' + suite + ' ----||\n' + '-'*(len(suite)+14))
		suite = unittest.TestLoader().loadTestsFromTestCase(getattr(sys.modules['__main__'], suite))
		unittest.TextTestRunner(verbosity=2).run(suite)