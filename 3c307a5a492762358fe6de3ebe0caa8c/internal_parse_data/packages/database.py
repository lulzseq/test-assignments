import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.sql import SQL, Identifier


class Database:

    def __init__(self, username: str, password: str, dbname: str, tablename: str) -> None:
        self.username = username
        self.password = password
        self.dbname = dbname
        self.tablename = tablename

    def create_table(self) -> None:
        conn = psycopg2.connect(dbname=self.dbname, user=self.username,
                                host='127.0.0.1', password=self.password)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(SQL('''
            CREATE TABLE {} (
                id serial PRIMARY KEY,
                datetime VARCHAR(255) NOT NULL,
                action VARCHAR(255) NOT NULL,
                method VARCHAR(255) NOT NULL,
                response VARCHAR(255) NOT NULL);
            ''').format(Identifier(self.tablename)))
        conn.close()

    def write_log(self, datetime: object, action: str, method: str, response: str) -> None:
        conn = psycopg2.connect(dbname=self.dbname, user=self.username,
                                host='127.0.0.1', password=self.password)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(SQL('''INSERT INTO {} (datetime, action, method, response) VALUES (%s, %s, %s);''').format(
            Identifier(
                self.tablename)), (datetime, action, method, response))
        conn.close()
