import json
import os
from datetime import datetime

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class DBConnector():
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            **json.loads(os.getenv("DB"))
        )
        assert self.connection.is_connected(), "Соединение с БД не установлено"

    def db_request(self, query: tuple[str, list | None]) -> list:
        self.cursor = self.connection.cursor()
        self.cursor.execute(*query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        return data

    def __get_new_id(self, table: str, field: str = "id") -> int:
        max_id = self.db_request(
            (f"""SELECT MAX({field}) FROM {table}""",)
        )[0][0]
        return max_id + 1

    def create_user(self, username: str) -> int:
        uid = self.__get_new_id("wp_users")
        dt = datetime.now()
        self.db_request(
            (
                """INSERT INTO wp_users (id, user_login, user_registered) \
                    VALUES (%s, %s, %s)""", [uid, username, dt]
            )
        )
        return uid

    def get_user_by_id(self, uid: int) -> list:
        return self.db_request(
            (
                """SELECT user_login, user_email FROM wp_users \
                        WHERE id = %s""", [uid]
            )
        )

    def delete_user(self, uid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_users WHERE id = %s""", [uid])
        )

    def create_page(self, title: str) -> int:
        pid = self.__get_new_id("wp_posts")
        dt = datetime.now()
        self.db_request(
            (
                """INSERT INTO wp_posts (id, post_title, post_excerpt, \
                    post_content, post_date, post_date_gmt, post_modified, \
                        post_modified_gmt, post_content_filtered, to_ping, \
                            pinged) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, \
                                %s, %s, %s)""",
                [pid, title, title, title, dt, dt, dt, dt, "", "", ""]
            )
        )
        return pid

    def get_page_by_id(self, pid: int) -> list:
        return self.db_request(
            ("""SELECT post_title FROM wp_posts WHERE id = %s""", [pid])
        )

    def delete_page(self, pid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_posts WHERE id = %s""", [pid])
        )

    def create_post(self, title: str) -> int:
        pid = self.__get_new_id("wp_posts")
        dt = datetime.now()
        self.db_request(
            (
                """INSERT INTO wp_posts (id, post_title, post_excerpt, \
                    post_content, post_date, post_date_gmt, post_modified, \
                        post_modified_gmt, post_content_filtered, to_ping, \
                            pinged) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, \
                                %s, %s, %s)""",
                [pid, title, title, title, dt, dt, dt, dt, "", "", ""]
            )
        )
        return pid

    def get_post_by_id(self, pid: int) -> list:
        return self.db_request(
            ("""SELECT post_title FROM wp_posts WHERE id = %s""", [pid])
        )

    def delete_post(self, pid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_posts WHERE id = %s""", [pid])
        )

    def create_comment(self, content: str) -> int:
        cid = self.__get_new_id("wp_comments", "comment_id")
        dt = datetime.now()
        self.db_request(
            (
                """INSERT INTO wp_comments (comment_id, comment_content, \
                    comment_author, comment_date, comment_date_gmt) \
                        VALUES (%s, %s, %s, %s, %s)""",
                [cid, content, "Firstname.LastName", dt, dt]
            )
        )
        return cid

    def get_comment_by_id(self, cid: int) -> list:
        return self.db_request(
            (
                """SELECT comment_content, comment_post_ID FROM wp_comments \
                    WHERE comment_ID = %s""", [cid]
            )
        )

    def delete_comment(self, cid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_comments WHERE comment_id = %s""", [cid])
        )

    def disconnect(self) -> None:
        self.connection.close()
