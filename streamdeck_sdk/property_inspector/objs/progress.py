from string import Template
from typing import Optional

from .base import BasePIElement


class Progress(BasePIElement):
    def __init__(
            self,
            label: str,
            uid: str,
            max_value: float = 1,
            default_value: float = 0,
            left_label: Optional[str] = None,
            right_label: Optional[str] = None,
    ):
        self.left_label = left_label
        self.right_label = right_label
        self.max_value = max_value
        self.label = label
        self.default_value = default_value
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"
        self.onchange = f"onchange_{self.uid}"

    def get_html_element(self) -> str:
        left_label = f"<span>{self.left_label}</span>" if self.left_label else ""
        right_label = f"<span>{self.right_label}</span>" if self.right_label else ""

        res = f"""
    <div class="sdpi-item" type="progress">
        <div class="sdpi-item-label">{self.label}</div>
        {left_label}
        <progress class="sdpi-item-value" id="{self.uid}" value="{self.default_value}" max="{self.max_value}">
        </progress>
        {right_label}
    </div>
        """
        return res

    def get_js_code(self) -> str:
        return ""

    def get_on_connect_js(self) -> str:
        template = Template("""
        if (settings["${uid}"] !== undefined) {
            ${js_el_const}.value = settings.${uid}
        } else {
            settings["${uid}"] = ${js_el_const}.value
        }
        """)
        res = template.substitute(uid=self.uid, js_el_const=self.js_el_const)

        return res

    def get_js_consts(self) -> str:
        res = f"""
    const {self.js_el_const} = document.getElementById("{self.uid}")
        """
        return res
