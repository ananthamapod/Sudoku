from random import randint

original_board = [
    [1, 0, 3, 0],
    [0, 0, 0, 0],
    [2, 0, 4, 0],
    [0, 0, 0, 0]
]

n = 10

fixed = set([(0, 0),(0, 2),(2, 0),(2, 2)])

def heuristic(board):
    collisions = 0
    for i in range(4):
        for j in range(4):
            val = board[i][j]
            for n in range(4):
                if n != i and board[n][j] == val:
                    collisions += 1

            for m in range(4):
                if m != j and board[i][m] == val:
                    collisions += 1

            squareX = j // 2
            squareY = i // 2

            for n in range(2):
                for m in range(2):
                    if not (2 * squareX + m == j or 2 * squareY + n == i) and board[2 * squareY + n][2 * squareX + m] == val:
                        collisions += 1
    return collisions

def deepcopy_board(board):
    ret = []
    for row in board:
        ret_row = []
        for elem in row:
            ret_row.append(elem)
        ret.append(ret_row)
    return ret

def generate_successor(board):
    choices = [
        [1,3],
        [0,1,2,3],
        [1,3],
        [0,1,2,3]
    ]
    row = randint(0,3)
    index1 = randint(0, len(choices[row])-1)
    del choices[row][index1]
    index2 = randint(0, len(choices[row])-1)
    del choices[row][index2]
    ret = deepcopy_board(board)
    ret[row][index2], ret[row][index1] = ret[row][index1], ret[row][index2]
    return ret

def generate_board(board, fixed):
    choices = [
        [2,4],
        [1,2,3,4],
        [1,3],
        [1,2,3,4]
    ]

    for i in range(4):
        for j in range(4):
            if (i,j) not in fixed:
                index = randint(0, len(choices[i])-1)
                board[i][j] = choices[i][index]
                del choices[i][index]

def solver():
    solved = False
    solution = None
    boards = []
    # generate initial set
    for i in range(n):
        board = deepcopy_board(original_board)
        generate_board(board, fixed)
        boards.append(board)
    ## reset boards list to take both heuristics and states
    boards = [(heuristic(board), board) for board in boards]

    while not solved:
        # order by heuristic value of boards
        boards.sort(key=lambda x: x[0])
        # take top 10 (lower heuristic values)
        boards = boards[:10]
        # check first board
        if boards[0][0] == 0:
            # if heuristic is 0, set solved to true and set as solution
            solved = True
            solution = boards[0][1]
        else:
            # else, generate successors and loop
            ## generate successor boards
            successors = []
            for board in boards:
                for i in range(4):
                    successors.append(generate_successor(board[1]))
            ## add each successor to current list with heuristic value
            for s in successors:
                boards.append((heuristic(s), s))

    return solution

print solver()
