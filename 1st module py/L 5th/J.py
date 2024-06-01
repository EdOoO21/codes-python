import sys


class Student:
    def __init__(self, email: str, full_name: str):
        self.mark = {'exam': [], 'test': [], 'hw': []}
        self.email = email
        self.full_name = full_name

    def put_mark(self, mark: int, kind='hw'):
        if kind != 'hw' and kind != 'exam' and kind != 'test':
            raise TypeError
        else:
            if kind == 'exam':
                if len(self.mark['exam']) == 0:
                    self.mark['exam'] += [mark]
                else:
                    raise IndexError
            else:
                self.mark[kind] += [mark]

    def change_mark(self, num: int, new_mark: int, kind='hw'):
        if kind != 'hw' and kind != 'exam' and kind != 'test':
            raise TypeError
        else:
            if len(self.mark[kind]) <= num:
                raise IndexError
            self.mark[kind][num] = new_mark

    def get_result(self, ndigits=2):
        a = 0
        if len(self.mark['hw']) != 0:
            a += (sum(self.mark['hw']) / len(self.mark['hw'])) * 0.3

        if len(self.mark['test']) != 0:
            a += (sum(self.mark['test']) / len(self.mark['test'])) * 0.3

        if len(self.mark['exam']) != 0:
            a += (sum(self.mark['exam']) / len(self.mark['exam'])) * 0.4

        return round(a, ndigits)

    def marks_count(self, kind='hw'):
        return len(self.mark[kind])

    def __str__(self):
        return f'{self.email} {self.full_name}'


student = Student("test@yandex.ru", "Ivanov Ivan")
print(student)
student.put_mark(4, 'hw')
student.put_mark(10, 'exam')
print(student.get_result())
print(student.marks_count('hw'))
