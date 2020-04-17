def read_sudoku(grid_number):
    if grid_number < 10:
        grid_number = '0'+str(grid_number)
    else:
        grid_number = str(grid_number)
    with open(r'C:\Users\adria\conronawithlime\p096_sudoku.txt') as s:
        sudokus = s.readlines()
        sudokus = [line.strip('\n') for line in sudokus]
        idx = sudokus.index('Grid '+grid_number)+1
        sudoku = [list(map(int, num)) for num in sudokus[idx:idx+9]]

    return sudoku


def get_possible(y, x, puzzle):

    possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    column = puzzle[y]
    row = [position[x] for position in puzzle]
    grid_y, grid_x = 3*(y//3), 3*(x//3)
    grid = set()
    for i in range(3):
        for j in range(3):
            grid.add(puzzle[grid_y+i][grid_x+j])

    return possible - set(column) - set(row) - set(grid)


def solve(puzzle):
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                p = get_possible(y, x, puzzle)
                for num in p:
                    puzzle[y][x] = num
                    solve(puzzle)
                    puzzle[y][x] = 0

                return
    return


sudoku = read_sudoku(1)
solve(sudoku)
print(sudoku)


# nums = []
# for i in range(1, 51):
#     complete = None
#     sudoku = read_sudoku(i)
#     solve()
#     nums.append(int(''.join((str(i) for i in complete[0][:3]))))
# print(nums)
# print(sum(nums))

