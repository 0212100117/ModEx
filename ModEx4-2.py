class Player:

    def __init__(self, player_name, sports, average_score):
        self.name = player_name
        self.sport = sports
        self.score = average_score



    def show_stat(self):
        print(" Player Name             : ", self.name, "\n",
              "Player Sport            : ", self.sport, "\n",
              "Player Average Score    : ", self.score, "\n", )

    def update_stat(self):

        self.update_average_score = input("Input new Score: ")
        print(self.name, "'s", " Updated Average Score :", self.update_average_score, "\n")


player1 = Player("Neb", "Programming", 99)
player2 = Player("Norman", "bebe hunting", 100)
player3 = Player("Jayson", "Procrastinating", 99)

player1.show_stat()
player1.update_stat()
player2.show_stat()
player2.update_stat()
player3.show_stat()
player3.update_stat()
