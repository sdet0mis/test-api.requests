from dataclasses import dataclass, field

from faker import Faker


@dataclass
class PostPayloads:
    title: str = field(default_factory=Faker().pystr)
    status: str = "publish"
