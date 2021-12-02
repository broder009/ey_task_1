import sqlite3
import tqdm

from path import RESULT_FILE_PATH


class Database:
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        self.commit()
        return self.fetchall()

    def create_table(self):
        self.query("""CREATE TABLE IF NOT EXISTS data(data_id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT,
        lat_word TEXT,rus_word TEXT, int_num INT UNSIGNED, float_num DECIMAL(10,8));""")
        self.query("""CREATE INDEX IF NOT EXISTS int_float_nums_idx ON data(int_num, float_num);""")

    def insert_data(self):
        with open(RESULT_FILE_PATH) as f:
            lines = f.readlines()
            for line, i in zip(lines, tqdm.tqdm(range(len(lines)))):
                sep_line = line.removesuffix('\n').split('||')
                self.query("""INSERT INTO data (date, lat_word, rus_word, int_num, float_num) VALUES(?,?,?,?,?);""",
                           sep_line)

    def select_sum_avg(self):
        return self.query("SELECT SUM(int_num), AVG(float_num) FROM data")[0]

    def drop_table(self):
        self.query("""DROP TABLE data""")


