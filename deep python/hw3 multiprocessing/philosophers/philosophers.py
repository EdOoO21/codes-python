import threading
from enum import Enum
from typing import Callable
import logging
import time
from random import uniform
from typing import List

class Fork:
    def __init__(self, index: int):
        self.lock: threading.Lock = threading.Lock()
        self.index: int = index
        # Добавьте любые другие необходимые атрибуты

    def is_locked(self) -> bool:
        return self.lock.locked()


class PhilosopherState(Enum):
    THINKING = "thinking"
    HUNGRY = "hungry"
    EATING = "eating"

global dur
global startsat

class Philosopher(threading.Thread):
    def __init__(
        self,
        index: int,
        left_fork: Fork,
        right_fork: Fork,
        get_think_time: Callable[[], float],
        get_eat_time: Callable[[], float],
    ):
        super().__init__()
        self.index : int = index
        self.left_fork : Fork = left_fork
        self.right_fork : Fork = right_fork
        self.now = PhilosopherState.THINKING
        self.count = 0
        self.get_think_time = get_think_time
        self.get_eat_time = get_eat_time




    def run(self):
        global dur, startsat

        while (time.time() - startsat) <= dur:
            self.state = PhilosopherState.HUNGRY
            logging.info(f"Философ {self.index} голоден")

            left_acquired = self.left_fork.lock.acquire()
            right_acquired = self.right_fork.lock.acquire() if left_acquired else False

            if left_acquired and right_acquired:

                self.state = PhilosopherState.EATING
                self.count += 1
                logging.info(f"Философ {self.index} ест")
                time.sleep(self.get_eat_time())


                self.right_fork.lock.release()
                self.left_fork.lock.release()


                self.state = PhilosopherState.THINKING
                logging.info(f"Философ {self.index} думает")
                time.sleep(self.get_think_time())
            else:

                if left_acquired:
                    self.left_fork.lock.release()
                if right_acquired:
                    self.right_fork.lock.release()
            time.sleep(1)

    def is_eating(self) -> bool:
        return self.now == PhilosopherState.EATING

    def is_hungry(self) -> bool:
        return self.now == PhilosopherState.HUNGRY

    def is_thinking(self) -> bool:
        return self.now == PhilosopherState.THINKING

    def count_meals(self) -> int:
        return self.count


class Dinner:
    def __init__(
        self,
        num_philosophers,
        get_think_time: list[Callable[[], float]],
        get_eat_time: list[Callable[[], float]]
    ):
        self.num_philosophers = num_philosophers
        self.philosophers = [Philosopher(0, Fork(0), Fork(0), get_think_time[0],  get_eat_time[0]) for i in range(num_philosophers)]
        self.forks = [Fork(0) for i in range(num_philosophers)]
        self.index = 0

        for i in range(num_philosophers):
            if i == 0:
                self.forks[0] = Fork(0)
                left_fork = self.forks[0]
            else:
                left_fork = self.forks[i]
            if (i + 1) < num_philosophers:
                self.forks[i + 1] = Fork(i + 1)
                right_fork = self.forks[i + 1]
            else:
                right_fork = self.forks[0]
            self.philosophers[i] = Philosopher(i,  right_fork, left_fork, get_think_time[i], get_eat_time[i])

        # Инициализируйте вилки и философов
        # get_think_time и get_eat_time - список функций, которые возвращают время для размышления и еды для каждого философа

    def run_simulation(self, duration):
        global dur
        dur = duration
        global startsat
        startsat = time.time()


        for i,philosopher in enumerate(self.philosophers):
            if (time.time() - startsat) <= duration:
                self.index = i
                philosopher.start()
        self.stop_simulation()


    def stop_simulation(self):
        for philosopher in range(self.index):
            self.philosophers[philosopher].join()


