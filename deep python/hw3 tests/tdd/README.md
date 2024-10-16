### TDD

На лекции, как известно, мы проходили паттерн TDD (Test-Driven Development).

Напомним что это такое: 

* Вначале мы создаем тесты, которые должны падать для нашей текущей реализации программы
* После того, как мы написали тест, мы правим исходный код таким образом, чтобы программа отрабатывала все тесты

В этой задаче мы хотим сделать ровно все тоже самое.

Вам дается модуль с тестами (файл `test_task_manager.py`, где вам необходимо написать модуль реализации. Подсказка: лучше всего не пытаться написать код таким образом, чтобы он проходил все тесты, а скорее брать по тесту и писать реализацию (то есть буквально повторять шаги лекции)

Задача: реализовать таск-менеджер, который будет проходить все тесты написанные в модуле `test_task_manager.py`. Всю логику изучайте в написанных тестах!

**Дружеское напоминание**: В реализации вы должны обрабатывать случаи, где в тестах ожидается ошибка! (то есть иногда тест ожидает, что выпадет ошибка)