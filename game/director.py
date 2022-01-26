from game.card import Card


class Director:


    def __init__(self):

        self.card = 0
        self.is_playing = True
        self.score = 300
        self.guess = ''
        self.current_card = 0


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
        self.guess = input('Is the card higher or lower? [h/l] ').lower()
        self.current_card = card.value


    def do_updates(self):

        if not self.is_playing:
            return

        card = Card()
        card.scoring(self.current_card, self.guess)
        self.score += card.points
        self.current_card = card.value


    def do_outputs(self):

        if not self.is_playing:
            return

        print(f'Next card was: {self.current_card}')
        print(f'Your score is: {self.score}')
        self.is_playing = (self.score > 0)

    
    def play_again(self):

        if not self.is_playing:
            return

        roll_card = input("Play again? [y/n] ")
        print()
        self.is_playing = (roll_card == "y")