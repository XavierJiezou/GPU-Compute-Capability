from typing import Dict, List
import sqlite3
import json


class DB:
    def __init__(self, db_name: str) -> None:
        """Initialization

        Args:
            db_name (str): Name of the database file.
        """
        self.db_name = db_name

    def create_db(self) -> None:
        """Create a SQLite database.
        """
        conn = sqlite3.connect(self.db_name)
        conn.close()

    def create_table(self, table_name: str, columns: Dict) -> None:
        """Create a table in the database.

        Args:
            table_name (str): Name of the table to be created in the database.
            columns (Dict): Field name and type to be used when defining the table.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        arg = ','.join(
            [' '.join([k, str(v)]) for k, v in columns.items()]
        )
        sql = f'create table if not exists {table_name} ({arg})'
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def insert_rows(self, table_name: str, json_file: str) -> None:
        """Insert the data obtained from the json file into the table as rows.

        Args:
            table_name (str): Name of the table to be created in the database.
            json_file (str): A file in json format.
        """
        with open(json_file) as fp:
            data = json.load(fp)
        rows = {}
        for i in data:
            for j in data[i]:
                _id_list = data[i][j]['GPU']
                _cc_list = data[i][j]['Compute Capability']
                for _id, _cc in zip(_id_list, _cc_list):
                    rows[_id] = _cc
        rows = list(rows.items())
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        sql = f'insert into {table_name} values (?, ?)'
        cursor.executemany(sql, rows)
        conn.commit()
        cursor.close()
        conn.close()

    def select_gpus(self, table_name: str, columns: Dict, query: str) -> List:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        sql = f'select * from {table_name} where {list(columns.keys())[0]} like "%{query}%"'
        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res


def insert_rows(db_name: str, table_name: str, columns: Dict, json_file: str) -> None:
    db = DB(db_name)
    db.create_db()
    db.create_table(table_name, columns)
    db.insert_rows(table_name, json_file)


if __name__ == '__main__':
    db_name = 'cuda-gpus.db'
    table_name = 'GPUS'
    columns = {'ID': 'TEXT', 'CC': 'REAL'}
    # json_file='cuda-gpus.json'
    # insert_rows(db_name, table_name, columns, json_file)
    query = 'A10'
    res = DB(db_name).select_gpus(table_name, columns, query)
    print(res)
