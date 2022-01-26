import random


# TODO: Implement the Card class as follows...

# 1) Add the class declaration. Use the following class comment.

class Card:
    """
    The responsibility of Card is to keep track of the card number and calculate the points for 
    it.
   
    Attributes:
        value (int): The card value.
        points (int): The number of points the card is worth.
    """
    


# 2) Create the class constructor. Use the following method comment.


    """Constructs a new instance of Card with a value and points attribute.

    Args:
        self (Card): An instance of Card.
    """
    def __init__(self):
        self.value = int()
        self.points = int()
# 3) Create the roll(self) method. Use the following method comment.

    
    """Generates a new random value and calculates the points.
    
    Args:
        self (Card): An instance of Card.
    """
    def scoring(self, previous_card, guess):

        self.value = random.randint(1,13)
        if (guess == 'h' and self.value > previous_card) or (guess == 'l' and self.value < previous_card):
            self.points = 100
        elif (guess == 'h' and self.value < previous_card) or (guess == 'l' and self.value > previous_card):
            self.points = -75
        elif self.value == previous_card:
            self.points = 0
        

    def roll(self):
        self.value = random.randint(1,13)