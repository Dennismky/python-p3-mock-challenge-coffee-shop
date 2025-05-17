class Coffee:
    def __init__(self, name=""):
        self.name = name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) < 3:
            return "Name length must be greater or equal to 3"
        if hasattr(self, '_name'):
            return "cannot change coffee name"
        self._name = value
    

        
    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name=""):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if 1>= len(value) <=15:
            self._name = value
        else:
            return "name must be between 1 and 25"


    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass


    
class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        order.all_orders.append(self)

    @property
    def price(self):
        return self._name
    
    @price.setter
    def name(self, value):
        if 1.0 <  len(value) > 10.0:
            return "Price must be between 1.0 and 10.0"
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if hasattr("_name"):
            return "cannot change attrubute name"
        self._price = value

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            return "Customer must be a coffee class instance"
        self._customer = value
       
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            return ("Coffee must be instance of class Coffee")
        self._coffee = value

        


        


  




