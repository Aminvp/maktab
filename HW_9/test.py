import unittest
from datetime import date
from card import single_table_card, credit_card, credit_card_time


class TestSingleTableCardMethods(unittest.TestCase):
    
    def setUp(self):
        self.card = single_table_card(credit=1)
    
    def test_use_card(self):
        self.assertEqual(self.card.use(), 0)
        self.assertIsNot(self.card.use(), 1)


class TestCreditCardMethods(unittest.TestCase): 
    
    def setUp(self):
        self.card = credit_card(credit=5) 
    
    def test_use_card(self):
        self.assertEqual(self.card.use(), 4)
        self.card.charge(5)
        self.assertEqual(self.card.use(), 8)
        self.assertIsNot(self.card.use(), 9) 


class TestCreditCardTimeMethods(unittest.TestCase):
    
    def setUp(self):
        self.card = credit_card_time(credit=3, date=date(2021, 9, 5))
    
    def test_use_card(self):
        self.assertEqual(self.card.use(date(2021, 8, 20)), 2)
        self.card.charge(4, date(2021, 10, 5))
        self.assertEqual(self.card.use(date(2021, 10, 2)), 5)
        self.assertIsNot(self.card.use(date(2021,10, 6)), 5)
        self.assertIsNot(self.card.use(date(2021,10, 2)), 6)
    

unittest.main()
        
