from dataclasses import dataclass, field

from faker import Faker


@dataclass
class PagePayloads:
    title: str = field(default_factory=Faker().pystr)
