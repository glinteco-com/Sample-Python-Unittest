class HondaCar:
    speed_up_to_100 = 5  # secs
    brand = "Honda"
    name = None

    def __init__(self, name, price, driving_wheels=2, speed_up_to_100=10):
        self.name = name
        self.price = price
        self.driving_wheels = driving_wheels
        self.speed_up_to_100 = speed_up_to_100

    @property
    def is_fast(self):
        if self.speed_up_to_100 < 10:
            return True
        return False

    @property
    def pricing_type(self):
        if self.price < 25000:
            return "cheap"

        if self.price < 50000:
            return "normal"

        if self.price < 100000:
            return "expensive"

        return "super_expensive"

    def is_worth_to_buy_compared_with(self, car):
        is_price_better = self.price < car.price
        is_speed_better = self.speed_up_to_100 < car.speed_up_to_100
        is_driving_wheels_better = self.driving_wheels > car.driving_wheels
        comparisons = [is_price_better, is_speed_better, is_driving_wheels_better]
        return sum(comparisons) >= 2

    def
