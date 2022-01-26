import random


class Card:
    """
    The responsibility of Card is to keep track of the card number and calculate the points for 
    it.
   
    Attributes:
        value (int): The card value.
        points (int): The number of points the card is worth.
    """
    
    def __init__(self):
        self.value = int()
        self.points = int()

    
    def scoring(self, previous_card, guess):

        self.value = random.randint(2,14)
        if (guess == 'h' and self.value > previous_card) or (guess == 'l' and self.value < previous_card):
            self.points = 100
        elif (guess == 'h' and self.value < previous_card) or (guess == 'l' and self.value > previous_card):
            self.points = -75
        elif self.value == previous_card:
            self.points = 0
        

    def roll(self):
        self.value = random.randint(2,14)


    def card_display(self, card_number):
        if card_number == 14:
            return 'Ace'
        elif card_number == 11:
            return 'Jack'
        elif card_number == 12:
            return 'Queen'
        elif card_number == 13:
            return 'King'
        else:
            return str(card_number)
