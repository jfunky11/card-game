from game.card import Card


class Director:


    def __init__(self):

        self.card = 0
        self.is_playing = True
        self.score = 300
        guess = ''
        card = Card()
        card.roll()


    def start_game(self):

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()


    def get_inputs(self):

        card = Card()
        card.roll()
        print(f'The card is: {card.value}')
        guess = input('Is the card higher or lower? [h/l] ')

       
    def play_again(self):
        roll_card = input("play again? [y/n] ")
        self.is_playing = (roll_card == "y")


    def do_updates(self):

        if not self.is_playing:
            return

        card = Card()
        card.roll()
        self.score += card.points


    def do_outputs(self):

        if not self.is_playing:
            return

        card= Card()
        card.roll()
        
        print(f'Next card was: {card.value}')
        print(f'Your score is: {self.score}')
        self.is_playing == (self.score > 0)