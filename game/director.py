from game.dice import Die


class Director:


    def __init__(self):

        self.dice = 0
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        ##for i in range(5):
        die = Die()
        self.dice.append(die)

    def start_game(self):

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()

    def get_inputs(self):

        guess = input('is the dice higher or lower?')
       
    def play_again(self):
        roll_dice = input("play again? [y/n] ")
        self.is_playing = (roll_dice == "y")


    def do_updates(self):

        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):

        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"Your next dice : {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)