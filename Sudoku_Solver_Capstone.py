
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - ')

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')  # end tells to add nothing at the end instead of a new line once | printed

            if j == 8:
                print(board[i][j])  # \n not needed as print statement has \n at the end on default
            else:
                print(str(board[i][j]) + ' ', end='')


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None  # if no 0s are found


def valid(board, num, position):

    # Check Row
    for i in range(9):
        if board[position[0]][i] == num and i != position[1]:
            return False
    # Check Column
    for i in range(9):
        if board[i][position[1]] == num and i != position[0]:
            return False

    x = position[1] // 3 # Determine x position of box
    y = position[0] // 3 # Determine y position of box

    # Check Grid
    for i in range(y * 3, x * 3 +3 ):
        for j in range(x * 3, y * 3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True


def sudoku(board):
    found = find_empty(board)
    if not found:  # If no 0's found, board is solved
        return True
    else:          # Else return position of the 0
        row, column = found

    for i in range(1,10):
        if valid(board, i, (row, column)):  # check if solution is valid
            board[row][column] = i          # if valid, add solution to the board

            if sudoku(board):  # Try solve the next 0
                return True
            board[row][column] = 0  # If there isn't a valid solution, backtrack and make the previous square 0, and try
                                    # out a new solution for the number before that
    return None  # Backtrack (could have also returned False)

def player_board(sequence):
    result_2d_list = []

    # Iterate through the input string in groups of 9 characters
    for i in range(0, 81, 9):
        # Extract a group of 9 characters
        row = sequence[i:i + 9]

        # Convert each character to an integer and store them in a list
        row_list = [int(char) for char in row]

        # Append the row list to the result_2d_list
        result_2d_list.append(row_list)
    return result_2d_list


puzzle = ''
while True:
    ask = input('Do you want to input a sudoku puzzle or use a stored one we have? \nType i to input or s for stored: ')
    if ask == 'i':
        while True:
            puzzle = input('Type in the puzzle (comma separated if you want), with 0 for empty boxes: ').replace(' ', '').replace(',', '')
            if puzzle.isdigit() and len(puzzle) == 81:
                board = player_board(puzzle)
                break
            else:
                print('Input isn\'t 81 digits')
        break
    if ask == 's':
        break

print('')
print_board(board)
start_time = time.time()  # Record time to solve the board
sudoku(board)
end_time = time.time()
print('\n ___________________ \n')
print_board(board)
runtime = end_time - start_time
print(f"\nSudoku solving runtime: {runtime} seconds")
