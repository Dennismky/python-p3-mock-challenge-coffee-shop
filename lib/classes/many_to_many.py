class Coffee:
    def __init__(self, name=""):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise Exception("Cannot change coffee name")
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Name must be a string with at least 3 characters")

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)




class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Name must be a string between 1 and 15 characters")


    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        max_customer = None
        max_spent = 0

        for customer in cls.all:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > max_spent:
                max_spent = total
                max_customer = customer

        return max_customer


    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)  

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("Customer must be a Customer instance")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Coffee must be a Coffee instance")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, "_price")):
            self._price = price
        else:
            raise Exception("Price must be a float between 1.0 and 10.0")

        


        


  




