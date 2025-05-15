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
    username: Optional[str] = None
    name: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    url: str
    description: str
    link: HttpUrl
    locale: Optional[str] = None
    nickname: Optional[str] = None
    slug: str
    roles: Optional[List[str]] = None
    registered_date: Optional[str] = None
    capabilities: Optional[CapabilitiesModel] = None
    extra_capabilities: Optional[ExtraCapabilitiesModel] = None
    avatar_urls: AvatarUrlsModel
    meta: MetaModel | List
    _links: LinksModel


class DeletedUserModel(BaseModel):
    deleted: bool
    previous: UserModel
