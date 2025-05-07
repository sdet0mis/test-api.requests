import json
import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class DBConnector():
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            **json.loads(os.getenv("DB"))
        )
        assert self.connection.is_connected(), "Соединение с БД не установлено"

    def db_request(self, query: tuple[str, list]) -> list:
        self.cursor = self.connection.cursor()
        self.cursor.execute(*query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        return data

    def get_user_by_id(self, uid: int) -> list:
        return self.db_request(
            (
                """SELECT user_login, user_email FROM wp_users \
                        WHERE id = %s""", [uid]
            )
        )

    def get_page_by_id(self, pid: int) -> list:
        return self.db_request(
            ("""SELECT post_title FROM wp_posts WHERE id = %s""", [pid])
        )

    def get_post_by_id(self, pid: int) -> list:
        return self.db_request(
            ("""SELECT post_title FROM wp_posts WHERE id = %s""", [pid])
        )

    def get_comment_by_id(self, cid: int) -> list:
        return self.db_request(
            (
                """SELECT comment_content, comment_post_ID FROM wp_comments \
                    WHERE comment_ID = %s""", [cid]
            )
        )

    def disconnect(self) -> None:
        self.connection.close()
