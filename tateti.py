from random import randrange

initial_board = [ [1, 2, 3], [4, 'X', 6], [7, 8, 9]]
free_squares = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
player = True

def display_board(board):
    """ The function accepts one parameter containing the board's current status
     and prints it out to the console."""
    actual_board = board[:]
    for j in range(3):
        print("+--------+--------+--------+")
        print("|        |        |        |" )
        print(f'|   {actual_board[j][0]}    |   {actual_board[j][1]}    |   {actual_board[j][2]}    |')
        print("|        |        |        |" )
    print("+--------+--------+--------+")
    if player:
        victory_for(actual_board, "X")
    else:
        victory_for(actual_board, "O")

def enter_move(board):
    """  The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision."""

    move = int(input("Enter your move, please: "))
    if move < 1 or move > 9:
        return
    for i in range(3):
        for j in range(3):
            if board[i][j] == move and board[i][j] != "O" and board[i][j] != "X":
                board[i][j] = "O"

    global player
    player =  not player
    display_board(board)

def make_list_of_free_fields(board):
    """The function browses the board and builds a list of all the free squares; 
    the list consists of tuples, while each tuple is a pair of row and column numbers."""
    my_free_squares = free_squares[:]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                my_free_squares.remove((i,j))
    return my_free_squares

def victory_for(board, sign):
    """ The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game"""
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
    (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        print(f'Ha ganado {sign}')
        new_game()
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            print(f'Ha ganado {sign}')
            new_game()
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            print(f'Ha ganado {sign}')
            new_game()
    my_free_squares = make_list_of_free_fields(board)
    if len(my_free_squares) == 0:
        print("es un empate")
        new_game()
    if player:
        enter_move(board)
    draw_move(board)

def draw_move(board):
    """The function draws the computer's move and updates the board."""
    my_free_squares = make_list_of_free_fields(board)
    next_move = randrange(len(my_free_squares))
    board[my_free_squares[next_move][0]][my_free_squares[next_move][1]] = 'X'
    global player
    player =  not player
    display_board(board)

def new_game():
    '''Create a new game'''
    ask= input("Do you want to play again? (y/n): ")
    if ask == 'n':
        print("See u soon ;)")
        exit()
    if ask == 'y':
        global player
        player = True
        new_board = initial_board[:]
        display_board(new_board)


display_board([ [1, 2, 3], [4, 'X', 6], [7, 8, 9]])
