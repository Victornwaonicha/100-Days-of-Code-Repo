"""This code snippet is a unit test for the Customer class using Python's built-in unittest framework."""


import unittest  # unittest: This is the built-in module for creating and running tests.
from customer import Customer  # Customer: The Customer class is imported from the customer module.


class TestCustomer(unittest.TestCase): # TestCustomer: This class inherits from unittest.TestCase, making it a test case class.

    def setUp(self): # setUp Method: This method is run before each test method to set up any state that is shared across tests.
        """Customer Instances: Two instances of the Customer class are created, self.customer_1 and self.customer_2, with different initial values."""
        self.customer_1 = Customer("John", "Brad", 5000)
        self.customer_2 = Customer("Tina", "Smith", 3000)


    def test_customer_email(self): # test_customer_email Method: This test checks the customer_mail property.
        """Assertions: assertEqual checks if the customer_mail property of customer_1 and customer_2 matches the expected email addresses."""
        self.assertEqual(self.customer_1.customer_mail, "John.Brad@gmail.com")
        self.assertEqual(self.customer_2.customer_mail, "Tina.Smith@gmail.com")


    def test_customer_fullname(self): # test_customer_fullname Method: This test checks the customer_fullname property.
        """Assertions: assertEqual checks if the customer_fullname property of customer_1 and customer_2 matches the expected full names."""
        self.assertEqual(self.customer_1.customer_fullname, "John Brad")
        self.assertEqual(self.customer_2.customer_fullname, "Tina Smith")


    def test_apply_discount(self): # test_apply_discount Method: This test checks the apply_discount method.
        """Method Calls: The apply_discount method is called for both customer_1 and customer_2."""
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()

        """Assertions: assertEqual checks if the purchase attribute of customer_1 and customer_2 matches the expected discounted values."""
        self.assertEqual(self.customer_1.purchase, 4750)
        self.assertEqual(self.customer_2.purchase, 2850)


if __name__ == "__main__": # Main Block: This ensures that the test case runs when the script is executed directly.
    unittest.main()
