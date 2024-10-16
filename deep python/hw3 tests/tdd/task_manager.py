class TaskManager:
    def __init__(self):
        # YOUR REALIZATION HERE
        self.tasks = []

    def add_task(self, name):
        if (name == '') or (name is None):
            raise ValueError('Задача не может быть пустой и должна быть строкой!')
        self.tasks.append(name)
        return None

    def get_all_tasks(self):
        return self.tasks

    def process_next_task(self):
        if not self.tasks:
            raise IndexError("Нет задач для обработки.")
        if self.tasks[0] is None:
            raise Exception("Ошибка при обработке задачи")
        self.tasks.pop(0)
        return None

    def remove_task(self,name):
        try:
            self.tasks.remove(name)
        except ValueError:
            raise ValueError(f"Задача '{name}' не найдена.")
        return None

