import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 1
        self.player_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def find_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            print(f"It's a tie! Both chose {player_choice}.")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print(f"You win this round! {player_choice} beats {computer_choice}.")
            self.player_wins += 1
        else:
            print(f"Computer wins this round! {computer_choice} beats {player_choice}.")
            self.computer_wins += 1

    def check_winner(self):
        if self.player_wins > self.rounds // 2:
            return "player"
        elif self.computer_wins > self.rounds // 2:
            return "computer"
        return None

    def play_game(self):
        print("\n******Rock-Paper-Scissors!****** ")
        print(f"First to win {self.rounds // 2 + 1} rounds wins the game!")

        while self.current_round <= self.rounds:
            print(f"\n Round {self.current_round} ")

            player_choice = input("Enter rock, paper, or scissors: ").lower()
            while player_choice not in ["rock", "paper", "scissors"]:
                print(" Invalid choice. Try again.")
                player_choice = input("Enter rock, paper, or scissors: ").lower()

            computer_choice = self.get_computer_choice()
            print(f" Computer chose: {computer_choice}")

            self.find_winner(player_choice, computer_choice)

            game_winner = self.check_winner()
            if game_winner:
                print(f"\ {game_winner.upper()} wins the game! ")
                break
            self.current_round += 1
        print("\nFinal Score:")
        print(f"Player Wins: {self.player_wins}")
        print(f"Computer Wins: {self.computer_wins}")
        print("Thanks for playing! ")
        
num_rounds = int(input("Enter the number of rounds to play: "))
game = Rock_paper_scissors(num_rounds)
game.play_game()
