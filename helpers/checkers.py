import allure
from pydantic import BaseModel, ValidationError


class Checkers:

    @staticmethod
    @allure.step("Проверить статус код {expected_code}")
    def check_status_code(expected_code: int, actual_code: int) -> None:
        assert expected_code == actual_code, f"\n \
    Ожидаемый статус код: {expected_code}\n \
    Фактический статус код: {actual_code}"

    @staticmethod
    def validate(model: BaseModel, data: dict) -> BaseModel:
        try:
            return model.model_validate(data)
        except ValidationError as e:
            raise AssertionError(e)
