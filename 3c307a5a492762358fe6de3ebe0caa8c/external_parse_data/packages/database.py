import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.sql import SQL, Identifier

from .logger import log


class Database:

    def __init__(self, username, password, dbname, names):
        self.username = username
        self.password = password
        self.dbname = dbname
        self.tablename = dbname
        self.names = names

    def create_database(self):
        conn = psycopg2.connect(dbname='postgres', user=self.username,
                                host='127.0.0.1', password=self.password)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(SQL('''CREATE DATABASE {};''').format(Identifier(self.dbname)))
        conn.close()
        log('Create database: OK')

    def prepare_db(self):
        self.create_database()
        conn = psycopg2.connect(dbname=self.dbname, user=self.username,
                                host='127.0.0.1', password=self.password)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(SQL('''
            CREATE TABLE {} (
                id serial PRIMARY KEY,
                item_name VARCHAR(255) NOT NULL,
                url VARCHAR(255),
                price INTEGER);
            ''').format(Identifier(self.tablename)))
        log('Create table: OK')

        for name in self.names:
            cur.execute('''INSERT INTO ecomseller (item_name) VALUES (%s);''', (name,))
        conn.close()

    def match_data(self, name):
        conn = psycopg2.connect(dbname=self.dbname, user=self.username,
                                host='127.0.0.1', password=self.password)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(SQL('''
                SELECT *
                FROM {}
                WHERE item_name = %s;
            ''').format(Identifier(self.tablename)), (name,))

        response = cur.fetchall()
        conn.close()

        if len(response) == 0:
            log('Match data: NOT FOUND')
        else:
            log('Match data: OK')

        return response

    def update_item(self, id, url=None, price=None):
        conn = psycopg2.connect(dbname=self.dbname, user=self.username,
                                host='127.0.0.1', password=self.password)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(SQL('''UPDATE {}
                        SET url = %s, price = %s
                        WHERE id = %s;''').format(Identifier(self.tablename)), (url, price, id,))
        conn.close()
        return log('Item update: OK')

    def insert_item(self, name, url=None, price=None):

        if not name:
            return log('Insert new item: ERROR')

        conn = psycopg2.connect(dbname=self.dbname, user=self.username,
                                host='127.0.0.1', password=self.password)

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(SQL('''INSERT INTO {} (item_name, url, price) VALUES (%s, %s, %s);''').format(Identifier(
            self.tablename)), (name, url, price))
        conn.close()
        return log('Insert new item: OK')
