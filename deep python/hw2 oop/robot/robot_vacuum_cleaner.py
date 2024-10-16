from enum import Enum
from typing import Protocol


class Movable(Protocol):
    def turn(self, direction: "TurnDirection") -> None:
        ...

    def move(self, distance: int, move_direction: "Movement") -> None:
        ...


class VacuumCleaner:
    def __init__(self) -> None:
        self.dust_collected = 0  # Собранная пыль

    def vacuum(self):
        """Метод для всасывания пыли"""
        self.dust_collected += 1
        print(f"Впитывание пыли... Собрано {self.dust_collected} единиц пыли.")


class TurnDirection(Enum):
    LEFT = -1
    RIGHT = 1


class Movement(Enum):
    FORWARD = 1
    BACKWARD = -1


class Direction(Enum):
    NORTH = "N"
    WEST = 'W'
    EAST = 'E'
    SOUTH = 'S'


class SensorDirection(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    FRONT = 'front'

# Базовый класс для машины на радиоуправлении


class RemoteControlCar:
    def __init__(self) -> None:
        self.position = [0, 0]  # Начальная позиция
        self.direction = Direction.NORTH  # Направление: N, E, S, W

    def move(self, distance, direct):
        """Метод движения"""
        match direct:
            case Movement.FORWARD:
                match self.direction:
                    case Direction.NORTH:
                        self.position[1] += distance
                    case Direction.EAST:
                        self.position[0] += distance
                    case Direction.SOUTH:
                        self.position[1] -= distance
                    case Direction.WEST:
                        self.position[0] -= distance
                print(
                    f"Двигаемся вперед на {distance} \
                        единиц. Позиция: {self.position}")
            case Movement.BACKWARD:
                match self.direction:
                    case Direction.NORTH:
                        self.position[1] -= distance
                    case Direction.EAST:
                        self.position[0] -= distance
                    case Direction.SOUTH:
                        self.position[1] += distance
                    case Direction.WEST:
                        self.position[0] += distance
                print(
                    f"Двигаемся назад на {distance} единиц. \
                        Позиция: {self.position}")
            case _:
                raise AttributeError

    def turn(self, direct):
        """Поворот"""
        match direct:
            case TurnDirection.LEFT:
                directions = [
                    Direction.NORTH,
                    Direction.WEST,
                    Direction.SOUTH,
                    Direction.EAST]
                self.direction = directions[(
                    directions.index(self.direction) + 1) % 4]
                print(f"Поворот налево. Теперь направление: {self.direction}")
            case TurnDirection.RIGHT:
                directions = [
                    Direction.NORTH,
                    Direction.EAST,
                    Direction.SOUTH,
                    Direction.WEST]
                self.direction = directions[(
                    directions.index(self.direction) + 1) % 4]
                print(f"Поворот направо. Теперь направление: {self.direction}")
            case _:
                raise AttributeError


# Класс для автономного движения
class AutonomousMovement(Movable):
    def __init__(self) -> None:
        super().__init__()
        self.sensors = {
            SensorDirection.FRONT: False,
            SensorDirection.LEFT: False,
            SensorDirection.RIGHT: False}  # Ложь означает, что препятствий нет

    def detect_obstacle(self, direction) -> bool:
        """Метод для распознавания препятствия"""
        return self.sensors[direction]

    def auto_move(self) -> None:
        """Метод для автономного движения"""
        if not self.detect_obstacle(SensorDirection.FRONT):
            print("Препятствий впереди нет, едем вперед.")
            self.move(1, Movement.FORWARD)
        else:
            print("Обнаружено препятствие! Пытаемся объехать...")
            if not self.detect_obstacle(SensorDirection.LEFT):
                self.turn(TurnDirection.LEFT)
                self.move(1, Movement.FORWARD)
            elif not self.detect_obstacle(SensorDirection.RIGHT):
                self.turn(TurnDirection.RIGHT)
                self.move(1, Movement.FORWARD)
            else:
                print("Заблокирован со всех сторон. Остановка.")


# Итоговый класс автономного робота для уборки
class AutonomousCleaningRobot(
        VacuumCleaner,
        RemoteControlCar,
        AutonomousMovement):
    def __init__(self) -> None:
        VacuumCleaner.__init__(self)
        RemoteControlCar.__init__(self)
        AutonomousMovement.__init__(self)

    def clean_and_move(self) -> None:
        """Метод для автономной уборки и движения"""
        print("Начинаем уборку...")
        self.vacuum()  # Включаем всасывание
        self.auto_move()  # Автономное движение
