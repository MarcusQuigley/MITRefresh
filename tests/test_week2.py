import unittest

from problems import week2

class Week2_Tests(unittest.TestCase):
  def test_counting_vowels(self):
    str = 'test_counting_vowels'
    expected = 6
    actual = week2.counting_vowels(str)
    self.assertEqual(expected, actual)

  def test_counting_vowels2(self):
    str = 'xxxxx'
    expected = 0
    actual = week2.counting_vowels(str)
    self.assertEqual(expected, actual)

  def test_counting_bobs1(self):
    expected = 2
    str = 'azcbobobegghakl'
    actual = week2.counting_bobs(str)
    self.assertEqual(expected,actual)

  def test_counting_bobs2(self):
    expected = 1
    str = 'bob'
    actual = week2.counting_bobs(str)
    self.assertEqual(expected,actual)

  def test_order(self):
    order = 'salad water hamburger salad hamburger'
    expected = 'salad:2 hamburger:2 water:1'
    actual = week2.item_order(order)
    self.assertEqual(expected, actual)