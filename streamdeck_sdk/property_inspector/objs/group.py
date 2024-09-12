from typing import List

from .base import BasePIElement


class Group(BasePIElement):
    def __init__(
            self,
            items: List[BasePIElement],
            label: str = "",
    ):
        self.items = items
        self.label = label

    def get_html_element(self) -> str:
        items = "\n".join([element.get_html_element() for element in self.items])

        label = f'<div class="sdpi-item-label">{self.label}</div>' if self.label else ""

        res = f"""
    <div type="group" class="sdpi-item">
        {label}
        <div class="sdpi-item-group">
            {items}
        </div>
    </div>
        """
        return res

    def get_js_code(self) -> str:
        res = "\n".join([element.get_js_code() for element in self.items])
        return res

    def get_on_connect_js(self) -> str:
        res = "\n".join([element.get_on_connect_js() for element in self.items])
        return res

    def get_js_consts(self) -> str:
        res = "\n".join([element.get_js_consts() for element in self.items])
        return res

    def get_on_did_receive_settings_js(self) -> str:
        res = "\n".join([element.get_on_did_receive_settings_js() for element in self.items])
        return res
