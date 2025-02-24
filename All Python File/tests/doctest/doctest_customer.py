class Customer:
    """A Sample Customer Class"""

    discount = 0.95
    """Class Attribute: discount is a class attribute with a value of 0.95. 
       This attribute is shared among all instances of the class"""
    

    def __init__(self, first, last, purchase):
        self.first = first
        self.last = last
        self.purchase = purchase

    
    @property
    def customer_mail(self):
        """Property Decorator: @property makes the method customer_mail behave like an attribute."""
        return f"{self.first}.{self.last}@gmail.com"
    
    
    @property
    def customer_fullname(self):
        return f"{self.first} {self.last}"
    
    
    def apply_discount(self):
        self.purchase = int(self.purchase * self.dicountt)
        return self.purchase