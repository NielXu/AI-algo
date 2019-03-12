"""
Using Minimax algorithm to make the best moves in
game tic-tac-toe.
"""
class Game():
    def __init__(self):
        self.board = [["-" for x in range(3)] for x in range(3)]
        self.flag = 1
    
    def show(self):
        "Show the game board"
        for i in self.board:
            print(i)
    
    def move(self):
        "Return 1 if it is player move, 0 if computer move"
        return self.flag
    
    def place(self, x, y):
        "Make move, select (x,y)"
        if self.flag == 1:
            self.flag = 0
            self.board[x][y] = "O"
        else:
            self.flag = 1
            self.board[x][y] = "X"
    
    def end(self):
        "Check if player or computer win, return None if no one wins"
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '-':
                return 0 if self.board[i][0] == "X" else 1
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '-':
                return 0 if self.board[0][i] == "X" else 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
            return 0 if self.board[0][0] == "X" else 1
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
            return 0 if self.board[0][2] == "X" else 1
    
    def isfull(self):
        "Check if the board is full already"
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    return False
        return True
    
    def reset(self):
        self.board = [["-" for x in range(3)] for x in range(3)]
        self.flag = 1


def start():
    game = Game()
    flag = True
    game.show()
    while flag:
        result = game.end()
        if result is not None:
            if result == 1:
                print("GameOver, Player win!")
                flag = restart(game)
            else:
                print("GameOver, Computer win!")
                flag = restart(game)
        else:
            if game.isfull():
                print("GameOver, Draw!")
                flag = restart(game)
            else:
                rnd = game.move()
                if rnd == 1:
                    mv = input("Eneter your move:")
                    x,y = mv.split(",")
                    game.place(int(x), int(y))
                else:
                    mv = input("Computer move:")
                    x,y = mv.split(",")
                    game.place(int(x), int(y))
                game.show()

def restart(game):
    again = input("Do you wanna try again?(y/n)")
    if again == "y":
        print("=============")
        print("=============")
        print("=============")
        game.reset()
        game.show()
        return True
    else:
        return False

start()