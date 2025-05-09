from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Optional


class GuidModel(BaseModel):
    rendered: str


class ContentModel(BaseModel):
    rendered: str
    protected: bool


class ExcerptModel(BaseModel):
    rendered: str
    protected: bool


class MetaModel(BaseModel):
    footnotes: str


class LinkModel(BaseModel):
    href: HttpUrl
    targetHints: Optional[Dict[str, List[str]]]


class LinksModel(BaseModel):
    self: List[LinkModel]
    collection: List[LinkModel]
    about: List[LinkModel]
    author: List[LinkModel]
    replies: List[LinkModel]
    version_history: List[LinkModel]
    wp_attachment: List[LinkModel]
    curies: List[Dict[str, str | bool]]


class PageModel(BaseModel):
    id: int
    date: str
    date_gmt: str
    guid: GuidModel
    modified: str
    modified_gmt: str
    slug: str
    status: str
    type: str
    link: HttpUrl
    title: GuidModel
    content: ContentModel
    excerpt: ExcerptModel
    author: int
    featured_media: int
    parent: int
    menu_order: int
    comment_status: str
    ping_status: str
    template: str
    meta: MetaModel
    class_list: List[str]
    _links: LinksModel


class DeletedPageModel(BaseModel):
    deleted: bool
    previous: PageModel
