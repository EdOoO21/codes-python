import sqlite3

import typing as tp


class FitnessDB:
    def __init__(self, db_name: str = "fitness.db") -> None:
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self) -> None:
        cursor = self.conn.cursor()

        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS t_client (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL
                    )
                ''')

        # шаблон-заготовка которую нужно будет дообновить в методе
        # add_table_m2m_membership(
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS t_membership (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        membership_type TEXT UNIQUE NOT NULL
                    )
                ''')

        # тут нужно будет добавить таблицу
        self.add_table_m2m_membership(cursor)

    def add_table_m2m_membership(self, cursor: sqlite3.Cursor) -> None:
        """
        тут будет ваше добавление связи, которое должно работать как м2м
        """
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS t_client_membership (
                    client_id INTEGER,
                    membership_id INTEGER,
                    FOREIGN KEY (client_id) REFERENCES t_client(id),
                    FOREIGN KEY (membership_id) REFERENCES t_membership(id),
                    PRIMARY KEY (client_id, membership_id)
                    )
                ''')

    def add_client(self, name: str) -> int | None:
        """
        Добавляет клиента в таблицу t_client.
        """
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO t_client (name) VALUES (?)', (name,))
        self.conn.commit()
        client_id = cursor.lastrowid
        cursor.close()
        return client_id

    def add_membership(self, membership_type: str) -> int | None:
        """
        Добавляет тип абонемента в таблицу t_membership.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO t_membership (membership_type) VALUES (?)',
            (membership_type,))
        self.conn.commit()
        membership_id = cursor.lastrowid
        cursor.close()
        return membership_id

    def link_client_and_membership(
            self,
            client_id: int,
            membership_id: int) -> None:
        """
        Связывает клиента и абонемент в таблице t_client_membership.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO t_client_membership (client_id, membership_id)
            VALUES (?, ?) ''', (client_id, membership_id))
        self.conn.commit()
        cursor.close()

    def get_client_membership(self,
                              client_name: str) -> tp.List[tp.Tuple[str]]:
        """
        Получает список абонементов для указанного клиента.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT t_membership.membership_type
        FROM t_client
        JOIN t_client_membership ON t_client.id = t_client_membership.client_id
        JOIN t_membership ON t_membership.id =t_client_membership.membership_id
        WHERE t_client.name = ?''', (client_name,))
        self.conn.commit()
        ans = cursor.fetchall()
        cursor.close()
        return ans
