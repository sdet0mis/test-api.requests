from dataclasses import dataclass, field

from faker import Faker


@dataclass
class UpdateUserPayloads:
    email: str = field(default_factory=Faker().email)


@dataclass
class CreateUserPayloads(UpdateUserPayloads):
    username: str = field(default_factory=Faker().user_name)
    password: str = field(default_factory=Faker().password)
