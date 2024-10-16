from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from types import TracebackType
from typing import Protocol
import hashlib
import json
import hashlib
import queue

class SupportsStr(Protocol):
    """Класс с абстрактным методом `__str__`."""

    @abstractmethod
    def __str__(self) -> str:
        """Привести тип к `str`"""


@dataclass
class StorageAdapter:
    """Адаптер базы данных."""
    _storage : dict
    operations : list

    def __init__(self, _storage_directory : Path):
        self._storage_directory = _storage_directory

        self._storage = {}
        self.operations = []

    def hashed(self,key) -> str:
        return hashlib.sha256(key.encode()).hexdigest()

    def get(self, key: SupportsStr) -> str | None:
        """Получить объект, если он существует."""
        path = Path.joinpath(self._storage_directory, self.hashed(key))
        if self._storage_directory.exists():
            if path.exists():
                try:
                    with path.open('r', encoding='utf-8') as file:
                        data = json.load(file)
                except json.JSONDecodeError:
                    path.unlink()
                    return None
                else:
                    if ("hash" in data) and ("value" in data):
                        if (self.hashed(key) == data.get("hash")):
                            return data.get("value")
                        else:
                            path.unlink()
                    else:
                        path.unlink()
                        # if self.hashed(key) in self._storage:
                        #     data = {
                        #         "hash" : self.hashed(key),
                        #         'value' : self._storage[self.hashed(key)],
                        #     }
                        #     with open(path, 'w') as json_file:
                        #         json.dump(data, json_file)
                        #     return self._storage[self.hashed(key)]
            else:
                # if len(self._storage) != sum([1 for _ in self._storage_directory.iterdir()]):
                #     if self.hashed(key) in self._storage:
                #         data = {
                #             "hash" : self.hashed(key),
                #             'value' : self._storage[self.hashed(key)],
                #         }
                #         with open(path, 'w') as json_file:
                #             json.dump(data, json_file)
                #         return self._storage[self.hashed(key)]
                return None
        else:
            self._storage_directory.mkdir()
        return None

    def update(self, key: SupportsStr, value: SupportsStr) -> None:
        """Обновить (или добавить) значение по ключу."""
        hashed_key = self.hashed(key)
        self.operations.append(('update', hashed_key, value))
        return None


    def delete(self, key: SupportsStr) -> None:
        """Удалить ключ вместе со значением."""
        self.operations.append(('delete', self.hashed(key)))
        return None


    def clear(self) -> None:
        """Удалить все ключи вместе со значениями."""
        self.operations.append('clear')
        return None


    def commit(self) -> None:
        """Подтвердить изменения."""
        for action in self.operations:
            if action[0] == 'update':

                if (self._storage_directory.exists()):
                    if (self._storage_directory.is_file() or self._storage_directory.is_symlink()):
                        self._storage_directory.unlink()
                        self._storage_directory.mkdir()
                else:
                    if self._storage_directory.is_symlink():
                        self._storage_directory.unlink()
                    self._storage_directory.mkdir(exist_ok=True)


                data = {
                    'hash' : action[1],
                    'value': action[2],
                }
                self._storage[action[1]] = action[2]
                with open(Path.joinpath(self._storage_directory , action[1]), 'w') as json_file:
                    json.dump(data, json_file)

            if action[0] == 'delete':
                if (self._storage_directory.exists()):
                    if (self._storage_directory.is_file() or self._storage_directory.is_symlink()):
                        self._storage_directory.unlink()
                        self._storage_directory.mkdir()
                else:
                    self._storage_directory.mkdir(exist_ok=True)

                if action[1] in self._storage:
                    self._storage.pop(action[1])
                path = Path.joinpath(self._storage_directory, action[1])
                if path.exists():
                    path.unlink()
            if action == 'clear':
                if (self._storage_directory.exists()):
                    if (self._storage_directory.is_file() or self._storage_directory.is_symlink()):
                        self._storage_directory.unlink()
                        self._storage_directory.mkdir()
                else:
                    self._storage_directory.mkdir(exist_ok=True)


                self._storage.clear()
                for file in self._storage_directory.iterdir():
                    if not file.is_dir():
                        file.unlink()
                    else:
                        self.dir_runner(file)
        self.operations.clear()

    def dir_runner(self, path : Path) :
        for file in path.iterdir():
            if not file.is_dir():
                file.unlink()
            else:
                self.dir_runner(file)


    def rollback(self) -> None:
        """Откатить неподтвержденные изменения."""
        self.operations.clear()
        return None

    def __getitem__(self, key: SupportsStr) -> str | None:
        """Получить объект, если он существует."""
        path = Path.joinpath(self._storage_directory, self.hashed(key))
        if self._storage_directory.exists():
            if path.exists():
                try:
                    with path.open('r', encoding='utf-8') as file:
                        data = json.load(file)
                except json.JSONDecodeError:
                    path.unlink()
                    return None
                else:
                    if ("hash" in data) and ("value" in data):
                        if (self.hashed(key) == data.get("hash")):
                            return data.get("value")
                        else:
                            path.unlink()
                    else:
                        path.unlink()
                        # if self.hashed(key) in self._storage:
                        #     data = {
                        #         "hash" : self.hashed(key),
                        #         'value' : self._storage[self.hashed(key)],
                        #     }
                        #     with open(path, 'w') as json_file:
                        #         json.dump(data, json_file)
                        #     return self._storage[self.hashed(key)]
            else:
                # if len(self._storage) != sum([1 for _ in self._storage_directory.iterdir()]):
                #     if self.hashed(key) in self._storage:
                #         data = {
                #             "hash" : self.hashed(key),
                #             'value' : self._storage[self.hashed(key)],
                #         }
                #         with open(path, 'w') as json_file:
                #             json.dump(data, json_file)
                #         return self._storage[self.hashed(key)]
                return None
        else:
            self._storage_directory.mkdir()
        return None

    def __setitem__(self, key: SupportsStr, value: SupportsStr) -> None:
        """Обновить (или добавить) значение по ключу."""
        hashed_key = self.hashed(key)
        self.operations.append(('update', hashed_key, value))
        return None

    def __delitem__(self, key: SupportsStr) -> None:
        """Удалить ключ вместе со значением."""
        self.operations.append(('delete', self.hashed(key)))
        return None

    def __enter__(self):
        """Открыть транзакцию."""
        return self


    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Закрыть транзакцию."""
        if (exc_type is None) and (exc_value is None) and (traceback is None):
            self.commit()
        else:
            self.rollback()
            raise

# adapter = StorageAdapter(Path('12'))
# adapter.symlink_to(adapter)

# with adapter:
#     adapter.update('KEY', 123)

# value = adapter.get('KEY')
# print(value)