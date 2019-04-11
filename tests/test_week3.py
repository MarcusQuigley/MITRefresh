import unittest
from problems import week3

class Week3_Tests(unittest.TestCase):
  def test_oddtuples(self):
    actual = week3.oddTuples((1,2,3,4,5,6))
    expected = (1,3,5)
    self.assertEqual(expected, actual)

  def test_oddtuples2(self):
    actual = week3.oddTuples2((1,2,3,4,5,6))
    expected = (1,3,5)
    self.assertEqual(expected, actual)

  def test_howManyValues(self):
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    expected = (4)

    self.assertEqual(expected, week3.howManyValues(animals))

  def test_largestValues(self):
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkeydonkeydonkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    expected = ('d')
    
    self.assertEqual(expected, week3.largestValues(animals))

  def test_nDigits(self):
    actual = week3.nDigits(12345)
    expected = 5
    self.assertEqual(expected, actual)

