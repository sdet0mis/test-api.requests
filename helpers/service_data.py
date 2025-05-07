from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


@dataclass
class ServiceDataModel:
    payloads: Optional[BaseModel]
    model: BaseModel
