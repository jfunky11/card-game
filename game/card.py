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
        """Initialization of values for Card Class
           .value carries the card number
           .points carries the point value for the card
        """
        self.value = int()
        self.points = int()

    
    def scoring(self, previous_card, guess):
        """Method for calculating the points that a card is worth.
           First it checks for the players guess and then compares their previous card to the new card
           to determine point allotment.        
        """
        self.value = random.randint(2,14)
        if (guess == 'h' and self.value > previous_card) or (guess == 'l' and self.value < previous_card):
            self.points = 100
        elif (guess == 'h' and self.value < previous_card) or (guess == 'l' and self.value > previous_card):
            self.points = -75
        elif self.value == previous_card:
            self.points = 0
        

    def roll(self):
        """Method for getting a new random value for a card.
        """
        self.value = random.randint(2,14)


    def card_display(self, card_number):
        """Method for returning a card name like 'Ace', 'King', 'Queen', or 'Jack'
           based on the card_value. Mainly used for displaying card names for the user.
        """
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
