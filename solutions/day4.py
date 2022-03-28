import copy


class Board:
    def __init__(self, rows: list):
        self.rows = rows
        self.columns = []
        for i in range(len(self.rows)):
            column = []
            for j in range(len(self.rows[i])):
                column.append(self.rows[j][i])
            self.columns.append(column)
            column = []

    def check_if_won(self, numbers: list):
        for row in self.rows:
            if set(row).issubset(numbers):
                return True
        for column in self.columns:
            if set(column).issubset(numbers):
                return True
        return False

    def determine_score(self, numbers: list) -> int:
        tile_score = 0
        for row in self.rows:
            for number in row:
                if number not in numbers:
                    tile_score += int(number)
        last_number = int(numbers[-1])
        return(tile_score * last_number)


class Game:
    def __init__(self, winning_numbers, boards):
        self.winning_numbers = copy.deepcopy(winning_numbers)
        self.played_numbers = []
        self.boards = copy.deepcopy(boards)

    def check_4_winner(self):
        for board in self.boards:
            if board.check_if_won(self.played_numbers):
                return board
        return False

    def new_number(self) -> None:
        number = self.winning_numbers.pop(0)
        self.played_numbers.append(number)


with open('../inputs/day4.txt', 'r') as f:
    data = list(f)

    for i in range(len(data)):
        data[i] = data[i].strip('\n').split(' ')

    for i in range(len(data)):
        data[i] = (list(filter(lambda x: x != '', data[i])))

winning_numbers = data.pop(0)
winning_numbers = winning_numbers[0].split(',')
boards, board = [], []

for line in data:
    if line != []:
        board.append(line)
    else:
        if board != []:
            board_object = Board(board)
            boards.append(board_object)
            board = []

board_object = Board(board)
boards.append(board_object)
game = Game(winning_numbers, boards)

# part one
while game.check_4_winner() is False:
    game.new_number()

winning_board = game.check_4_winner()
score = winning_board.determine_score(game.played_numbers)

print(f'\nthe first winning board is \n{winning_board.rows}\nIts score is {score}\n')

# part two
game2 = Game(winning_numbers, boards)
while len(game2.boards) != 0:
    while game2.check_4_winner() is False:
        game2.new_number()
    current_winning_board = game2.check_4_winner()
    game2.boards.remove(current_winning_board)

last_board = current_winning_board
score = last_board.determine_score(game2.played_numbers)
print(f'the last winning board is \n{last_board.rows}\nIts score is {score}\n')
