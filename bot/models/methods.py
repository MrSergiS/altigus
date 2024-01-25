from bot.config.config import DatabaseConfig
from psycopg2 import Error, pool
from typing import Union


class DatabaseCursor:

    def __init__(self, config: DatabaseConfig):
        self.connect = pool.SimpleConnectionPool(minconn=1, maxconn=10,
                                                 database=config.database,
                                                 user=config.user,
                                                 password=config.password,
                                                 host=config.host,
                                                 port=config.port
                                                 )

    def call_connect(self, query: str, method: Union[None, str] = None, param: tuple = ()):
        try:
            conn = self.connect.getconn()
            cursor = conn.cursor()
            cursor.execute(query, param)
            if method:
                result = getattr(cursor, method)()
                return result
            conn.commit()
        except Error as e:
            print(e)
        finally:
            self.connect.putconn(conn)

    def get_profession_count(self):
        query = 'SELECT COUNT(*) FROM job_alert;'
        res = self.call_connect(query, 'fetchone')
        if res:
            return res[0]
        return False

    def get_client_id(self, client_id: int):
        query = 'SELECT id FROM client WHERE client_id = %s;'
        return self.call_connect(query, 'fetchone', (client_id, ))[0]

    def get_user_config(self, client_id: int):
        query = 'SELECT client_name, language FROM client WHERE client_id = %s;'
        return self.call_connect(query, 'fetchone', (client_id, ))

    def update_client_language(self, client_id: int, language: str):
        query = 'UPDATE client SET language = %s WHERE client_id = %s;'
        return self.call_connect(query, param=(language, client_id))

    def create_client(self, client_id: int, name: str, language: str):
        query = 'INSERT INTO client (client_id, client_name, language) VALUES (%s, %s, %s);'
        return self.call_connect(query, param=(client_id, language, name))

    def get_result(self, client_id: int):
        query = 'SELECT result FROM result WHERE client_id = %s'
        return self.call_connect(query, 'fetchall', (client_id, ))[-1]

    def get_result_alert(self, result_hash: str):
        query = 'SELECT title, short_description, full_description, ' \
                'min_salary_germany, max_salary_germany, min_salary_latvia, ' \
                'max_salary_latvia, reason' \
                ' FROM job_alert WHERE intro = %s AND sensin = %s AND think = %s AND percep = %s'
        return self.call_connect(query, 'fetchall', tuple(result_hash))

    def fields_name(self, table_name: str):
        query = f'SELECT column_name FROM information_schema.columns WHERE table_name = %s;'
        result = self.call_connect(query, param=(table_name, ))
        return [field_name[0] for field_name in result].remove('id')

    def create_new_quiz(self, data):
        keys = [k for k in data.keys()]
        values = tuple(v for v in data.values())
        query = f'INSERT INTO quiz ({", ".join(keys)}) VALUES ({"%s, " * 22}%s);'
        return self.call_connect(query, param=values)

    def quiz_field_up(self, client_id: int, value: str):
        query = 'INSERT INTO result (client_id, result) VALUES (%s, %s)'
        return self.call_connect(query, param=(client_id, value))
