import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      stock = quote["stock"]
      top_bid_price = quote["top_bid"]["price"]
      ask_bid_price = quote["top_ask"]["price"]
      ratio = (top_bid_price + ask_bid_price) / 2

      self.assertEqual(getDataPoint(quote), (stock, top_bid_price, ask_bid_price, ratio))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      stock = quote["stock"]
      top_bid_price = quote["top_bid"]["price"]
      ask_bid_price = quote["top_ask"]["price"]
      ratio = (top_bid_price + ask_bid_price) / 2

      self.assertEqual(getDataPoint(quote), (stock, top_bid_price, ask_bid_price, ratio))

  def test_getRatio_calculatePriceAZero(self):
    self.assertEqual(getRatio(0, 5), 0)

  def test_getRatio_calculatePriceBZero(self):
    self.assertEqual(getRatio(5, 0), None)

  def test_getRatio_calculateValidValues(self):
    test_cases = {
      (5, 2): 5 / 2,
      (-2, 2): -2 / 2,
      (0, 1): 0,
      (1, 0): None
    }

    for (price_a, price_b), result in test_cases.items():
      self.assertEqual(getRatio(price_a, price_b), result)





if __name__ == '__main__':
    unittest.main()
