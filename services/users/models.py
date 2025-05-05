from typing import List, Dict, Any, Optional

from pydantic import BaseModel, RootModel, EmailStr, HttpUrl


class CapabilitiesModel(BaseModel):
    read: bool
    level_0: bool
    subscriber: bool


class ExtraCapabilitiesModel(BaseModel):
    subscriber: bool


class AvatarUrlsModel(RootModel):
    root: Dict[str, HttpUrl]


class MetaModel(BaseModel):
    persisted_preferences: List[Any]


class TargetHintsModel(BaseModel):
    allow: List[str]


class LinkModel(BaseModel):
    href: HttpUrl
    targetHints: Optional[TargetHintsModel]


class LinksModel(BaseModel):
    self: List[LinkModel]
    collection: List[LinkModel]


class UserModel(BaseModel):
    id: int
    username: str
    name: str
    first_name: str
    last_name: str
    email: EmailStr
    url: str
    description: str
    link: HttpUrl
    locale: str
    nickname: str
    slug: str
    roles: List[str]
    registered_date: str
    capabilities: CapabilitiesModel
    extra_capabilities: ExtraCapabilitiesModel
    avatar_urls: AvatarUrlsModel
    meta: MetaModel
    _links: LinksModel


class DeletedUserModel(BaseModel):
    deleted: bool
    previous: UserModel
