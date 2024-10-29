from philosophers import Dinner, Philosopher, Fork
from typing import List
import time,pytest
from random import uniform

class PhilosopherSimulationChecker:
    def __init__(self, dinner: Dinner):
        self.dinner : Dinner = dinner
        self.philosophers : List[Philosopher] = dinner.philosophers
        self.forks : List[Fork] = dinner.forks

    def check_deadlock(self) -> bool:
        """
        Check if the system is in a deadlock state.
        """

        return all(i.is_hungry() for i in self.philosophers)

    def check_starvation(self, timeout: int = 10) -> bool:
        """
        Check if any philosopher is starving (hasn't eaten for a long time).
        """

        for philosopher in self.philosophers:
            if philosopher.is_hungry():
                now = philosopher.count
                time.sleep(timeout)
                then = philosopher.count
                if now == then:
                    return True
        return False

    def check_mutual_exclusion(self) -> bool:
        """
        Check if no two adjacent philosophers are eating simultaneously.
        """

        for i in range(len(self.philosophers)):
            if (self.philosophers[i].is_eating()) and (self.philosophers[(i + 1) % len(self.philosophers)].is_eating()):
                return True
        return False

    def comprehensive_check(self, duration: float) -> bool:
        """
        Run a comprehensive check for a specified duration.
        """
        # assert (not self.check_deadlock()), 'deadlock'
        # assert (not self.check_starvation()), 'starving'
        # assert (not self.check_mutual_exclusion()), 'near'
        return (not self.check_deadlock()) and (not self.check_starvation()) and (not self.check_mutual_exclusion())


def test():
    num_philosophers = 5
    think_times = [lambda: uniform(0.1, 0.5) for _ in range(num_philosophers)]
    eat_times = [lambda: uniform(0.1, 0.5) for _ in range(num_philosophers)]
    duration = 5
    dinner = Dinner(num_philosophers, think_times, eat_times)
    checker = PhilosopherSimulationChecker(dinner)

    dinner.run_simulation(duration)

    assert not checker.check_deadlock(), "дедлок игра помойка"

    print([i.now for i in checker.philosophers])
    assert not checker.check_starvation(timeout=5), "голоден фрик"


    assert not checker.check_mutual_exclusion(), "бля по русски рядом сидящие хавают"


    result = checker.comprehensive_check(duration)
    assert result, "общий чек не прошел"

