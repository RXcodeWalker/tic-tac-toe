from player import Player


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

        player1_name = input("Enter Player 1 name (X): ")
        player2_name = input("Enter Player 2 name (O): ")

        self.player1 = Player(player1_name, "X")
        self.player2 = Player(player2_name, "O")

        self.current_player = self.player1
        self.draws = 0

    def display_board(self):
        display = []

        for i in range(9):
            if self.board[i] == " ":
                display.append(str(i + 1))
            else:
                display.append(self.board[i])

        print()
        print(f" {display[0]} | {display[1]} | {display[2]} ")
        print("---+---+---")
        print(f" {display[3]} | {display[4]} | {display[5]} ")
        print("---+---+---")
        print(f" {display[6]} | {display[7]} | {display[8]} ")
        print()

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        self.current_player = self.player1

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player.symbol
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if (
                self.board[a] ==
                self.board[b] ==
                self.board[c] != " "
            ):
                return self.board[a]

        return None

    def is_draw(self):
        return " " not in self.board

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def display_scoreboard(self):
        print("\n========================")
        print("      SCOREBOARD")
        print("========================")
        print(f"{self.player1.name} ({self.player1.symbol}): {self.player1.wins}")
        print(f"{self.player2.name} ({self.player2.symbol}): {self.player2.wins}")
        print(f"Draws: {self.draws}")
        print("========================\n")

    def play_single_game(self):
        while True:
            self.display_board()

            try:
                move = int(
                    input(
                        f"{self.current_player.name} ({self.current_player.symbol}), choose a position (1-9): "
                    )
                ) - 1

                if move < 0 or move > 8:
                    print("Please enter a number between 1 and 9.")
                    continue

                if not self.make_move(move):
                    print("That position is already occupied.")
                    continue

            except ValueError:
                print("Please enter a valid number.")
                continue

            winner = self.check_winner()

            if winner:
                self.display_board()

                print(f"{self.current_player.name} wins!")

                self.current_player.wins += 1

                break

            if self.is_draw():
                self.display_board()

                print("It's a draw!")

                self.draws += 1

                break

            self.switch_player()

    def play(self):
        print("\nWelcome to Tic-Tac-Toe!\n")

        while True:
            self.play_single_game()

            self.display_scoreboard()

            play_again = input(
                "Would you like to play again? (y/n): "
            ).lower()

            if play_again != "y":
                print("\nThanks for playing!")
                break

            self.reset_board()