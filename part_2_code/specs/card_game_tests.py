
import unittest

from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

   def setUp(self):
      self.card = Card("spades", 1)
      self.card1 = Card("spades", 2)
      self.card2 = Card("spades", 3)
      self.cards = [Card("spades", 1), Card("spades",2), Card("spades", 3)]


# Test the check_for_ace function, is passed Ace..

   def test_check_for_ace_true(self):
      self.assertEqual(True, CardGame.check_for_ace(self, self.card))


# Test the check_for_ace function, is not passed Ace..

   def test_check_for_ace_false(self):
      self.assertEqual(False, CardGame.check_for_ace(self, self.card1))


# Test the highest_card function..

   def test_highest_card(self):
      self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))


#  Test the cards_total function..

   def test_cards_total(self):
      self.assertEqual("You have a total of 6", CardGame.cards_total(self, self.cards))
  
