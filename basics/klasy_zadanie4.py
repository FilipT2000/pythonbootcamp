class Basket():

    def __init__(self, marka, max_zasieg):
        self.marka = "Tesla"
        self.zasieg = max_zasieg
        self.max_zasieg = max_zasieg

    def add_product(self, product, liczba):


    def count_total_price(self):
        self.zasieg = self.max_zasieg
        return self.zasieg

    def generate_report(self):


basket = Basket()
product = Product(1, "Woda", 10)
basket.add_product(product, 5)
basket.count_total_price()
basket.generate_report()



