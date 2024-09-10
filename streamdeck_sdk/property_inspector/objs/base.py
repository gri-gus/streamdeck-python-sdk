import re

from abc import ABC, abstractmethod

UID_PATTERN = re.compile(r'^[a-z][a-z0-9_]*$')
UIDS = []


def is_valid_uid(uid):
    if UID_PATTERN.match(uid):
        return True
    else:
        return False


class UidCheckMixin:
    def __setattr__(self, key, value):
        if key != "uid":
            return super().__setattr__(key, value)

        if value in UIDS:
            raise ValueError(f"uid must be unique. uid={value}")
        if not value:
            raise ValueError(f"uid must not be empty. uid={value}")
        if not isinstance(value, str):
            raise ValueError(f"uid must be str. uid={value}")
        if not is_valid_uid(uid=value):
            raise ValueError(f"uid does not match pattern {UID_PATTERN}. uid={value}")
        UIDS.append(value)
        return super().__setattr__(key, value)


class BaseElement(UidCheckMixin):
    pass


class BasePIElement(BaseElement, ABC):
    @abstractmethod
    def get_html_element(self) -> str:
        pass

    def get_js_code(self) -> str:
        return ""

    def get_on_connect_js(self) -> str:
        return ""

    def get_js_consts(self) -> str:
        return ""

    def get_on_did_receive_settings_js(self) -> str:
        return self.get_on_connect_js()
