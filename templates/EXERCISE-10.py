'''
In this exercise, you will need to create a simple Tic-Tac-Toe game that runs 
in the terminal using Python. Here are the steps to program it.

1. Define a 2d list to represent the game board. You can use the 
following letters and symbols to represent the players' moves: dash (-)
represents empty, 'X' represents Player 1 and 'O' represents Player 2.

2. Create a function named print_board to print the board on the 
terminal. This function should take the current state of the board as 
input and print it on the terminal in a user-friendly way.

3. Create a function named is_board_full that checks if the game 
board is full. The function should take the current state of the board as 
input and return False if it finds any empty position. If all the positions 
are filled with 'X' or 'O', it returns True indicating that the board is full.

4. Create a function named check_row that checks for a win in a row. 
The function should take the current state of the board as input and
return True if there is a win, else False.

5. Create a function named check_column that checks for a win in a 
column. The function should take the current state of the board as 
input and return True if there is a win, else False.

6. Create a function named check_diagonal that checks for a win in a
diagonal. The function should take the current state of the board as 
input and return True if there is a win, else False.

7. Write a function named get_move that prompts the player to enter a 
row and a column to make their move on the game board. Make sure 
to check if the move is valid, and if the position is already taken by a 
player. If the move is valid, the function should returns a tuple (row, 
col) containing the row and column entered by the player. If the 
position is not empty/invalid, prints a message telling the player that 
the position is already taken and prompts them to enter a new move 
by continuing the loop.

8. Write the main game loop. Here is the pseudocode:
board = [[-, -, -], [-, -, -], [-, -, -]]
players = [X, O]
current_player = 0
while True:
    print_baord(board)

    # Get player's move
    row, col = get_move(board)

    # Update board
    board[row][col] = players[current_player]
    
    # End game if a player wins
    if win_condition_is_met:
        print_board(board)
        print(current_player + ' wins')
        break
    
    # End Game if board is full
    if is_board_full(board):
        print_board(board)
        print('The game is a tie')
        break

    # Switch turn
    if current_player == 0:
        current_player = 1
    else:
        current_player = 0
'''