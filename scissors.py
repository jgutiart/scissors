import random

# Game Class
class Game:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()

    def start(self):
        print("Welcome to Rock, Paper, Scissors!")
        print("Choose a game mode:")
        print("1. Player vs Computer")
        print("2. Computer vs Computer")

        # Get the game mode choice from the player
        game_mode = input("Enter 1 or 2 to select a game mode: ")

        if game_mode == "1":
            self.play_player_vs_computer()
        elif game_mode == "2":
            self.play_computer_vs_computer()
        else:
            print("Invalid choice, please choose a valid game mode.")
            self.start()  # restart if invalid input

    def play_player_vs_computer(self):
        print("You are playing Player vs Computer!")
        # Get the player's choice
        player_choice = self.player.choose_move()
        # Get the computer's choice
        computer_choice = self.computer.choose_move()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = self.determine_winner(player_choice, computer_choice)
        print(result)

    def play_computer_vs_computer(self):
        print("You are playing Computer vs Computer!")
        # Get the computer's first choice
        computer_choice_1 = self.computer.choose_move()
        # Get the computer's second choice
        computer_choice_2 = self.computer.choose_move()

        print(f"Computer 1 chose: {computer_choice_1}")
        print(f"Computer 2 chose: {computer_choice_2}")

        # Determine the winner
        result = self.determine_winner(computer_choice_1, computer_choice_2, is_computer_vs_computer=True)
        print(result)

    def determine_winner(self, choice1, choice2, is_computer_vs_computer=False):
        if choice1 == choice2:
            return "It's a tie!"
        # Winning conditions
        if (choice1 == "rock" and choice2 == "scissors") or \
           (choice1 == "scissors" and choice2 == "paper") or \
           (choice1 == "paper" and choice2 == "rock"):
            if is_computer_vs_computer:
                return f"Computer 1's {choice1.capitalize()} beats Computer 2's {choice2.capitalize()}! Computer 1 wins!"
            else:
                return f"{choice1.capitalize()} beats {choice2.capitalize()}! You win!"
        if is_computer_vs_computer:
            return f"Computer 2's {choice2.capitalize()} beats Computer 1's {choice1.capitalize()}! Computer 2 wins!"
        return f"{choice2.capitalize()} beats {choice1.capitalize()}! You lose!"

# Player Class
class Player:
    def choose_move(self):
        while True:
            # Ask player for input
            player_choice = input("Enter your move (rock, paper, or scissors): ").lower()
            if player_choice in ["rock", "paper", "scissors"]:
                return player_choice
            else:
                print("Invalid choice, please choose again.")

# Computer Class
class Computer:
    def choose_move(self):
        moves = ["rock", "paper", "scissors"]
        return random.choice(moves)

# Main code
if __name__ == "__main__":
    game = Game()
    game.start()