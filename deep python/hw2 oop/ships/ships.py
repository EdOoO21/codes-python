import random


class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.positions = []

    def place(self, positions):
        self.positions = positions

    def hit(self) -> bool:
        self.hits += 1
        return self.hits == self.size

    def is_sunk(self):
        return self.hits == self.size


class Battleship(Ship):
    def __init__(self):
        self.size = 4


class Cruiser(Ship):
    def __init__(self):
        self.size = 3


class Destroyer(Ship):
    def __init__(self):
        self.size = 2


class Submarine(Ship):
    def __init__(self):
        self.size = 1


class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[" " for _ in range(self.size)]
                     for __ in range(self.size)]

    def is_valid_position(self, positions):
        for i in positions:
            if (i[0] < 0) or (i[1] < 0) \
                    or (i[0] >= self.size) or (i[1] >= self.size):
                return False
            if (self.grid[i[0]][i[1]] != ' '):
                return False
            if (((i[0] != self.size - 1) and (self.grid[i[0] + 1][i[1]] == 'S')) or
                ((i[0] != 0) and (self.grid[i[0] - 1][i[1]] == 'S')) or
                    ((i[1] != self.size - 1) and (self.grid[i[0]][i[1] + 1] == 'S')) or
                    ((i[1] != 0) and (self.grid[i[0]][i[1] - 1] == 'S'))):
                return False
        return True

    def place_ship(self, ship, start_row, start_col, horizontal=True):
        if not horizontal:
            if self.is_valid_position(
                    [(x, start_col) for x in \
                    range(start_row, start_row + self.size)]):
                for i in range(ship.size):
                    self.grid[start_row][start_col] = 'S'
                    start_row += 1
                return True
            else:
                return False
        else:
            if self.is_valid_position(
                    [(start_row, x) for x in range(start_col, start_col + self.size)]):
                for i in range(ship.size):
                    self.grid[start_row][start_col] = 'S'
                    start_col += 1
                return True
            else:
                return False


    def receive_shot(self, row, col):
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            return True
        else:
            self.grid[row][col] = 'O'
            return False

    def display(self):
        for i in self.grid:
            print(*i)

    def display_hidden(self):
        for i in self.grid:
            for y in i:
                if y != 'S':
                    print(y, end=" ")
                else:
                    print(" ", end=" ")
            print()

    def all_ships_sunk(self):
        for i in self.grid:
            for y in i:
                if y == 'S':
                    return False
        return True


def place_ships_on_board(ships, board):
    for i in ships:
        while True:
            horisontal = (1 == random.randint(0, 1))
            if horisontal:
                x, y = [random.randint(0, board.size - 1) for _ in range(2)]
                if (x + i.size - 1) <= board.size - 1:
                    for i in range(i.size) :
                        board.grid[x][y] = 'S'
                        x += 1
                    break
                if (x - i.size + 1) >= 0:
                    for i in range(i.size):
                        board.grid[x][y] = 'S'
                        x -= 1
                    break
            else:
                x, y = [random.randint(0, board.size - 1) for _ in range(2)]
                if (y + i.size - 1) <= board.size - 1:
                    for i in range(i.size) :
                        board.grid[x][y] = 'S'
                        y += 1
                    break
                if (y - i.size + 1) >= 0:
                    for i in range(i.size):
                        board.grid[x][y] = 'S'
                        y -= 1
                    break


def main():
    player_board = Board()
    opponent_board = Board()

    ships = [
        Battleship(),
        Cruiser(),
        Cruiser(),
        Destroyer(),
        Destroyer(),
        Destroyer(),
        Submarine(),
        Submarine(),
        Submarine(),
        Submarine()]

    # Размещение кораблей игрока
    place_ships_on_board(ships, player_board)

    # Размещение кораблей противника
    place_ships_on_board(ships, opponent_board)

    print("Ваше поле (Сверху) и поле противника (снизу):")
    player_board.display()
    print("\nПоле противника:")
    opponent_board.display_hidden()

    while not opponent_board.all_ships_sunk():
        try:
            row = int(input("Введите номер строки для выстрела (0-9): "))
            col = int(input("Введите номер столбца для выстрела (0-9): "))
            if row < 0 or row >= opponent_board.size or col < 0 or col >= opponent_board.size:
                print("Некорректные координаты, попробуйте снова.")
                continue
            hit = opponent_board.receive_shot(row, col)
            if hit:
                print("Попадание!")
            else:
                print("Промах!")

            print("Ваше поле (Сверху) и поле противника (снизу):")
            player_board.display()
            print("\nПоле противника:")
            opponent_board.display_hidden()

        except ValueError:
            print("Пожалуйста, вводите числа.")

    print("Все корабли противника потоплены! Игра окончена.")


if __name__ == "__main__":
    main()
