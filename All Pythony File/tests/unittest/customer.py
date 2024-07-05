class Customer:
    """A Sample Customer Class"""

    discount = 0.95
    """Class Attribute: discount is a class attribute with a value of 0.95. 
       This attribute is shared among all instances of the class"""
    

    def __init__(self, first_name, last_name, purchase):
        """Constructor Method: __init__ initializes an instance of the Customer class."""
        """Instance Attributes: first_name, last_name, and 
        purchase are instance attributes initialized using the constructor parameters."""
        self.first_name = first_name
        self.last_name = last_name
        self.purchase = purchase

    
    @property
    def customer_mail(self):
        """Property Decorator: @property makes the method customer_mail behave like an attribute."""
        return f"{self.first_name}.{self.last_name}@gmail.com"
    
    
    @property
    def customer_fullname(self):
        return f"{self.first_name} {self.last_name} is purchaing for {self.purchase}"
    
    
    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)


victor = Customer("Victor", "Moore", 5000)
"""Instance Creation: An instance of the Customer class is created with 
   the first_name "Victor", last_name "Moore", and purchase amount 5000."""


print(victor.customer_fullname)
"""Accessing Property: The customer_fullname property of the victor instance is accessed, 
   which triggers the method decorated with @property."""