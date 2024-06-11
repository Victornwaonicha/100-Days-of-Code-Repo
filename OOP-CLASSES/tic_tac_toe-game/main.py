def print_matrix(matrix):
    for row in matrix:
        print(row)

# print_matrix(tictactoe_matrix)

def play(row, column, player, board):
    if (row > 2 or column > 2):
        print("Invalid index")
        return
    
    if (row < 0 or column < 0):
        print("Invalid index")
        return

    if (player > 2 or player < 1):
        print("invalid player")
        return

    if board[row][column] != 0:
        print("Cannot play that box")
        return

    board[row][column] = player
    print(f"Player {player} played, your turn")

def check_win(matrix):
    # check horizontal winner
    ans = False
    player: int
    for row in matrix:
        # [1, 1, 1]
        ans = (row[0] == row[1] == row[2]) & (row[0] != 0)
        player = row[0]
        if ans:
             print(f"the winner is Player {player}")
             return True
    # check vertically
    for col in range(len(matrix[0])):
        #  when col = 0
        # [1, 0, 0]
        # [1, 0, 0]
        # [1, 0, 0]
        #  when col = 1
        # [0, 1, 0]
        # [0, 1, 0]
        # [0, 1, 0]
        # when col = 2
        # [0, 0, 1]
        # [0, 0, 1]
        # [0, 0, 1]

        ans = (matrix[0][col] == matrix[1][col] == matrix[2][col]) & (matrix[0][col] != 0)
        player = matrix[0][col]
        if ans:
             print(f"the winner is Player {player}")
             return True
    
    # check diagonal
    ans = (matrix[0][0] == matrix[1][1] == matrix[2][2]) & (matrix[0][0] != 0)
    # [1, 0, 0]
    # [0, 1, 0]
    # [0, 0, 1]
    player = matrix[0][0]
    if ans:
         print(f"the winner is Player {player}")
         return True

    ans = (matrix[0][2]== matrix[1][1] == matrix[2][0]) & (matrix[0][2])
    # [0, 0, 1]
    # [0, 1, 0]
    # [1, 0, 0]
    player = matrix[0][0]

    if ans:
         print(f"the winner is Player {player}")
         return True
    

    print("No winner yet")

    return False


def check_draw(matrix):
    for row in matrix:
        if 0 in row:
            return False
    return True


   

    

from art import art  
import os

def main():

    player = 1

    tt_matrix = [[0, 0, 0], 
                 [0, 0, 0], 
                 [0, 0, 0]]

    print(f"\033[35;1m{art}\033[0m")
    print_matrix(tt_matrix)
    print("Time to play")
    
    while True:
        row = int(input("select a row: "))
        col = int(input("select a column: "))

        play(row=row, column=col, board=tt_matrix, player=player)
        print_matrix(tt_matrix)
        won = check_win(matrix=tt_matrix)
        if won:
            input("Game completed! Do you want to play again? Type 'yes' or 'no': ") == "yes"
            os.system('clear')
            main()
        

        if check_draw(matrix=tt_matrix):
            input("The game is a draw. Do you want to play again? Type 'yes' or 'no': ") == "yes"
            os.system('clear')
            main()
        

        

        if player == 1:
            player = 2
        else:
            player = 1


        


if __name__ == '__main__':
    main()
