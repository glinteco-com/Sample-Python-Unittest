import unittest

from cars.honda import HondaCar


class TestHondaCar(unittest.TestCase):
    setupclass_calls = 0
    teardownclass_calls = 0

    def setUp(self):
        TestHondaCar.setup_calls += 1
        print(f"setup_calls: {TestHondaCar.setup_calls}")

        self.cheap_car = HondaCar("Jazz", 14000, driving_wheels=2, speed_up_to_100=15)
        self.normal_car = HondaCar("Jazz", 29000, driving_wheels=2, speed_up_to_100=12)
        self.expensive_car = HondaCar("Accord", 67000, driving_wheels=4, speed_up_to_100=7)
        self.super_expensive_car = HondaCar("HSV-010 GT", 990000, driving_wheels=4, speed_up_to_100=5)

    @classmethod
    def setUpClass(cls):
        cls.setup_calls = 0
        cls.teardown_calls = 0

        cls.setupclass_calls += 1
        print(f"setupclass_calls: {cls.setupclass_calls}")

    def tearDown(self):
        TestHondaCar.teardown_calls += 1
        print(f"teardown_calls: {TestHondaCar.teardown_calls}")

    @classmethod
    def tearDownClass(cls):
        cls.teardownclass_calls += 1
        print(f"teardownclass_calls: {cls.teardownclass_calls}")

    def test_is_fast_return_true(self):
        self.assertTrue(self.expensive_car.is_fast)

    def test_is_fast_return_false(self):
        self.assertFalse(self.cheap_car.is_fast)

    def test_pricing_type_return_cheap(self):
        self.assertEqual(self.cheap_car.pricing_type, "cheap")

    def test_pricing_type_return_normal(self):
        self.assertEqual(self.normal_car.pricing_type, "normal")

    def test_pricing_type_return_expensive(self):
        self.assertEqual(self.expensive_car.pricing_type, "expensive")

    def test_pricing_type_return_super_expensive(self):
        self.assertEqual(self.super_expensive_car.pricing_type, "super_expensive")

    def test_is_worth_to_buy_compared_with(self):
        self.assertFalse(self.cheap_car.is_worth_to_buy_compared_with(self.normal_car))

        self.assertFalse(self.cheap_car.is_worth_to_buy_compared_with(self.super_expensive_car))

        self.assertTrue(self.super_expensive_car.is_worth_to_buy_compared_with(self.cheap_car))
