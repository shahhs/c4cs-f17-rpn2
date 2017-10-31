import unittest

import rpn

class TestBasics(unitTest.TestCase): 
	def test_add(self): 
		result = rpm.calculate('1 1 +')
		self.assertEqual(2,result)
