from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


@dataclass
class ServiceDataModel:
    model: BaseModel
    payloads: Optional[BaseModel] = None
