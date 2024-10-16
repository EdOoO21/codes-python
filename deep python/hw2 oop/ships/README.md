### Ships

Задача на то, чтобы реализовать игру морской бой. Вам нужно реализовать два класса: `Ship` и `Board`.

Класс `Ship`
Это базовый класс, представляющий корабль. У корабля есть:

```
size: размер (например, длина корабля в клетках).
hits: количество попаданий по кораблю.
positions: список клеток на доске, занимаемых кораблём.
```

Методы:
```
place: задаёт позиции корабля на доске.
hit: увеличивает количество попаданий по кораблю и проверяет, потоплен ли он.
is_sunk: проверяет, потоплен ли корабль (если количество попаданий равно размеру корабля).
```
Наследники класса `Ship`
Здесь созданы специфические корабли с фиксированным размером:
```
Battleship — четырёхклеточный.
Cruiser — трёхклеточный.
Destroyer — двухклеточный.
Submarine — одноклеточный.
```
Все они наследуются от Ship и просто передают разные размеры в базовый класс.

```
Класс Board
Это класс, который управляет состоянием доски:

size: размер доски (по умолчанию 10x10).
grid: сама доска, представленная как двумерный массив, где пустая клетка обозначена пробелом (' '),
а занятая клетка обозначена символом корабля ('S').
```
Основные методы:

* `is_valid_position`: проверяет, можно ли разместить корабль в заданных координатах.
Этот метод учитывает соседние клетки, чтобы корабли не касались друг друга.
* `place_ship`: размещает корабль на доске, если его можно расположить по указанным координатам.
* `receive_shot`: обрабатывает выстрел по указанной клетке. Если в клетке есть корабль, то это считается попаданием, иначе — промах.
* `display`: выводит текущую доску (с видимыми кораблями).
* `display_hidden`: выводит доску, скрывая позиции кораблей (например, для показа противнику).
* `all_ships_sunk`: проверяет, потоплены ли все корабли на доске.

Метод для размещения кораблей `place_ships_on_board` - эта функция берёт список кораблей и случайным образом размещает их на доске, проверяя возможность их корректного размещения.

Мы вам оставим код для запуска игры, чтобы вы поиграли на досуге (а также для собственной проверки):

```python
def main():
    player_board = Board()
    opponent_board = Board()
    
    ships = [Battleship(), Cruiser(), Cruiser(), Destroyer(), Destroyer(), Destroyer(), 
             Submarine(), Submarine(), Submarine(), Submarine()]
    
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
```