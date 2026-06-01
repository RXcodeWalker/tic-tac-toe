class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
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
                self.board[a] == self.board[b] ==
                self.board[c] != " "
            ):
                return self.board[a]

        return None

    def is_draw(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Enter positions from 1 to 9.")

        while True:
            self.display_board()

            try:
                move = int(
                    input(
                        f"Player {self.current_player}, choose a position (1-9): "
                    )
                ) - 1

                if move < 0 or move > 8:
                    print("Invalid position.")
                    continue

                if not self.make_move(move):
                    print("That spot is already taken.")
                    continue

            except ValueError:
                print("Please enter a number.")
                continue

            winner = self.check_winner()

            if winner:
                self.display_board()
                print(f"Player {winner} wins!")
                break

            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()