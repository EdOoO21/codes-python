### Random

В Python, как и в других языках программирования имеется возможность получать случайное число.

Вы спросите зачем?

* нужен непредсказуемый ответ
* защита данных
* математика и алгоритмы
* тестирование))

В этой задаче вы должны познакомиться с возможностью патчинга методов. \
Работать будем с `random`. \
Конкретно, вам необходимо добиться того чтобы вызов функции `broken_random` выдавал только блатные числа (назовем их
номерными знаками). В текущей реализации этого нет и вам нужно это поддержать - а именно получившееся число в результате рандома привести к ближайшему блатному.

Список блатных номеров: `111 222 333 444 555 666 777 888 999`

Для этого предлагаем воспользоваться этой [библиотекой](https://docs.python.org/dev/library/unittest.mock.html).

Здесь вы дожны заменить реальный вызов рандома на вызов `patch_random` который будет "подгонять" число к блатному. Обратите внимание, что мы вызываем рандомное число в диапазоне от 100 до 1000


