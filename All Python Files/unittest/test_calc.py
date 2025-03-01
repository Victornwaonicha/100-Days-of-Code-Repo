"""DRY(DON"T REPEAT YOURSELF)"""


import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10 , 5)
        self.assertEqual(result, 15)


    def test_substract(self):
        result = calc.substract(10 , 5)
        self.assertEqual(result, 5)


    def test_multiply(self):
        result = calc.multiply(10 , 5)
        self.assertEqual(result, 50)

    """THE IMPLIMENTATION BELOW IS THE SAME AS ABOVE"""
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)


        # self.assertRaises(ValueError, calc.divide, 10, 0)

        """USING CONTEXT MANAGER WHEN TEST EXCEPTIONS"""
        with self.assertRaises(ValueError):
            calc.divide(10, 0)



"""IN ORDER TO RUN OUR TEST DIRECTLY FROM THE 
   SOURCE CODE AND ALLOW RUN THE CODE IN THE COMMAND LINE 
   USING JUST 'PYTHON3 THEN THE NAME OF OF FILE', WE DO THE BELOW"""

if __name__ == '__main__':
    unittest.main()