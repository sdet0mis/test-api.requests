import json
import os
from dataclasses import make_dataclass, field
from datetime import datetime

import allure
import mysql.connector
from dotenv import load_dotenv

from services.users.payloads import CreateUserPayloads
from services.pages.payloads import PagePayloads
from services.posts.payloads import PostPayloads
from services.comments.payloads import CreateCommentPayloads

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

    @allure.step("Создать пользователя")
    def create_user(self, **kwargs: dict) -> int:
        uid = self.__get_new_id("wp_users")
        username = CreateUserPayloads(**kwargs).username
        dt = datetime.now()
        self.db_request(
            (
                """INSERT INTO wp_users (id, user_login, display_name, \
                    user_registered) VALUES (%s, %s, %s, %s)""",
                [uid, username, username, dt]
            )
        )
        return make_dataclass(
            "User",
            [
                ("id", int, field(default=uid)),
                ("username", str, field(default=username))
            ]
        )

    @allure.step("Получить пользователя")
    def get_user_by_id(self, uid: int) -> list:
        return self.db_request(
            (
                """SELECT user_login, user_email FROM wp_users \
                        WHERE id = %s""", [uid]
            )
        )

    @allure.step("Удалить пользователя")
    def delete_user(self, uid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_users WHERE id = %s""", [uid])
        )

    @allure.step("Создать страницу")
    def create_page(self, **kwargs: dict) -> int:
        pid = self.__get_new_id("wp_posts")
        title = PagePayloads(**kwargs).title
        dt = datetime.now()
        self.db_request(
            (
                """INSERT INTO wp_posts (id, post_title, post_excerpt, \
                    post_content, post_date, post_date_gmt, post_modified, \
                        post_modified_gmt, post_type, post_content_filtered, \
                            to_ping, pinged) VALUES (%s, %s, %s, %s, %s, %s, \
                                %s, %s, %s, %s, %s, %s)""",
                [pid, title, title, title, dt, dt, dt, dt, "page", "", "", ""]
            )
        )
        return make_dataclass(
            "Page",
            [
                ("id", int, field(default=pid)),
                ("title", str, field(default=title))
            ]
        )

    @allure.step("Получить страницу")
    def get_page_by_id(self, pid: int) -> list:
        return self.db_request(
            ("""SELECT post_title FROM wp_posts WHERE id = %s""", [pid])
        )

    @allure.step("Удалить страницу")
    def delete_page(self, pid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_posts WHERE id = %s""", [pid])
        )

    @allure.step("Создать статью")
    def create_post(self, **kwargs: dict) -> int:
        pid = self.__get_new_id("wp_posts")
        title = PostPayloads(**kwargs).title
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
        return make_dataclass(
            "Post",
            [
                ("id", int, field(default=pid)),
                ("title", str, field(default=title))
            ]
        )

    @allure.step("Получить статью")
    def get_post_by_id(self, pid: int) -> list:
        return self.db_request(
            ("""SELECT post_title FROM wp_posts WHERE id = %s""", [pid])
        )

    @allure.step("Удалить статью")
    def delete_post(self, pid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_posts WHERE id = %s""", [pid])
        )

    @allure.step("Создать комментарий")
    def create_comment(self, **kwargs: dict) -> int:
        cid = self.__get_new_id("wp_comments", "comment_id")
        content = CreateCommentPayloads(**kwargs).content
        dt = datetime.now()
        self.db_request(
            (
                """INSERT INTO wp_comments (comment_id, comment_content, \
                    comment_author, comment_date, comment_date_gmt) \
                        VALUES (%s, %s, %s, %s, %s)""",
                [cid, content, "Firstname.LastName", dt, dt]
            )
        )
        return make_dataclass(
            "Comment",
            [
                ("id", int, field(default=cid)),
                ("content", str, field(default=content))
            ]
        )

    @allure.step("Получить комментарий")
    def get_comment_by_id(self, cid: int) -> list:
        return self.db_request(
            (
                """SELECT comment_content, comment_post_ID FROM wp_comments \
                    WHERE comment_ID = %s""", [cid]
            )
        )

    @allure.step("Удалить комментарий")
    def delete_comment(self, cid: int) -> None:
        self.db_request(
            ("""DELETE FROM wp_comments WHERE comment_id = %s""", [cid])
        )

    def disconnect(self) -> None:
        self.connection.close()
