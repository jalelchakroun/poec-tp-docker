import unittest

from calc import apply_vat

class TestCalc(unittest.TestCase):
  def test1(self):
    print("Start Test 1")
    final_percent = apply_vat(100.0, 20.0)
    self.assertEqual(final_percent, 120)
    print("End Test 1")

  def test2(self):
    print("Start Test 2")
    final_percent = apply_vat(55.25, 5.5)
    self.assertEqual(final_percent, 58.28874999999999)
    print("End Test 2")

  def test3(self):
    print("Start Test 3")
    final_percent = apply_vat(0.0, 10.0)
    self.assertEqual(final_percent, 0.0)
    print("End Test 3")

  def test4(self):
    print("Start Test 4")
    final_percent = apply_vat(-10.99, 10.0)
    self.assertEqual(final_percent, "Price ($-10.99) is negative")
    print("End Test 4")

  def test5(self):
    print("Start Test 5")
    final_percent = apply_vat("wrong value", 10.0)
    self.assertEqual(final_percent, "Price ($wrong value) is not a number")
    print("End Test 5")

  def test6(self):
    print("Start Test 6")
    final_percent = apply_vat(100.0, -10.0)
    self.assertEqual(final_percent, "Percentage (-10.0%) is not within these bounds")
    print("End Test 6")

  def test7(self):
    print("Start Test 7")
    final_percent = apply_vat(100.0, 110.0)
    self.assertEqual(final_percent, "Percentage (110.0%) is not within these bounds")
    print("End Test 7")

if __name__ == "__main__":
  unittest.main()
