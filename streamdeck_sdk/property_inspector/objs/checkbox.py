from string import Template
from typing import List

from .base import BasePIElement, BaseElement


class CheckboxItem(BaseElement):
    def __init__(
            self,
            uid: str,
            label: str = "",
            checked: bool = False,
    ):
        self.uid = uid
        self.label = label
        self.checked = checked
        self.js_el_const = f"{self.uid}_el"
        self.onchange = f"onchange_{self.uid}"

    def get_html_element(self) -> str:
        checked = "checked" if self.checked else ""
        label = self.label if self.label else ""

        res = f"""
            <div class="sdpi-item-child">
                <input class="sdpi-item-value" id="{self.uid}" type="checkbox" onchange="{self.onchange}()" 
                    {checked} >
                <label for="{self.uid}" class="sdpi-item-label">
                    <span></span>{label}
                </label>
            </div>
        """
        return res

    def get_js_code(self) -> str:
        template = Template("""
    const ${onchange} = () => {
        console.log(${js_el_const}.checked);
        settings["${uid}"] = ${js_el_const}.checked
        $$PI.setSettings(settings);
    }
        """)

        res = template.substitute(onchange=self.onchange, uid=self.uid, js_el_const=self.js_el_const)
        return res

    def get_on_connect_js(self) -> str:
        template = Template("""
        if (settings["${uid}"] !== undefined) {
            ${js_el_const}.checked = settings.${uid}
        } else {
            settings["${uid}"] = ${js_el_const}.checked
        }
        """)
        res = template.substitute(uid=self.uid, js_el_const=self.js_el_const)

        return res

    def get_on_did_receive_settings_js(self) -> str:
        return self.get_on_connect_js()

    def get_js_consts(self) -> str:
        res = f"""
    const {self.js_el_const} = document.getElementById("{self.uid}")
        """
        return res


class Checkbox(BasePIElement):
    def __init__(
            self,
            label: str,
            items: List[CheckboxItem],
    ):
        self.label = label
        self.items = items

    def get_html_element(self) -> str:
        items = "\n".join([element.get_html_element() for element in self.items])

        res = f"""
    <div type="checkbox" class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <div class="sdpi-item-value">
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
