from game.card import Card


class Director:
    """Director Class is designed to control the game structure and organization.
    """

    def __init__(self):
        """Initialization of variables used for Director Class methods:
           .card Card number
           .is-playing holds value for continuing the game
           .score holds value for players ongoing scoring
           .guess holds the value for the players guess of high or low
           .current_card holds the value of the current_card
        """
        self.card = 0
        self.is_playing = True
        self.score = 300
        self.guess = ''
        self.current_card = 0


    def start_game(self):
        """Method for structuring the order of events of game play
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()
        self.game_over()


    def get_inputs(self):
        """Method for getting user input about the players guess of high or low
           based on the display of the most recently drawn card.
        """
        card = Card()
        card.roll()
        card_string = card.card_display(card.value)
        print(f'The card is a {card_string}')
        self.guess = input('Is the card higher or lower? [h/l] ').lower()
        print()
        self.current_card = card.value


    def do_updates(self):
        """Method for updaing the ongoing score for the current game.
        """
        if not self.is_playing:
            return

        card = Card()
        card.scoring(self.current_card, self.guess)
        self.score += card.points
        self.current_card = card.value


    def do_outputs(self):
        """Method for displaying the 'next card' which is used for determining the score of the hand.
           Also outputs the players current score based on the scoring results of the 'next card'.
        """
        if not self.is_playing:
            return

        card = Card()
        card_string = card.card_display(self.current_card)
        print(f'Next card is a {card_string}')
        print(f'Your score is: {self.score}')
        self.is_playing = (self.score > 0)

    
    def play_again(self):
        """Method for getting input from the user on whether or not they want to play another hand.
           Ends the game if the player inputs 'n'.
        """
        if not self.is_playing:
            return

        roll_card = input("Play again? [y/n] ")
        print()
        self.is_playing = (roll_card == "y")
    
    def game_over(self):
        """Method for displaying 'Game Over' message.
        """
        print('Game Over')
