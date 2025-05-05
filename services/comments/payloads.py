from dataclasses import dataclass, field

from faker import Faker


@dataclass
class UpdateCommentPayloads:

    content: str = field(default_factory=Faker().pystr)


@dataclass
class CreateCommentPayloads(UpdateCommentPayloads):

    post: int = field(default_factory=Faker().pyint)
