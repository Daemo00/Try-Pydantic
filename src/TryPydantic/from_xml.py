"""Try importing Model from XML."""
from defusedxml.ElementTree import fromstring
from pydantic import BaseModel
from typing import Any
from pydantic.utils import GetterDict


class UserGetter(GetterDict):
    """Override getter to parse XML."""

    def get(self, key: Any, default: Any = None) -> Any:
        """Parse XML."""
        # element attributes
        if key in {'Id', 'Status'}:
            return self._obj.attrib.get(key, default)

        # element children
        else:
            try:
                return self._obj.find(key).attrib['Value']
            except (AttributeError, KeyError):
                return default


class User(BaseModel):
    """A User."""

    Id: int
    Status: str | None
    FirstName: str | None
    LastName: str | None
    LoggedIn: bool

    class Config:
        """Pydantic Configuration."""

        orm_mode = True
        getter_dict = UserGetter

    @classmethod
    def from_xml(cls, xml_string):
        """Parse XML."""
        user = User.from_orm(fromstring(xml_string))
        return user
