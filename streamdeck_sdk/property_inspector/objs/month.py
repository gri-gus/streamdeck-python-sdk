from string import Template
from typing import Optional

from .base import BasePIElement


class Month(BasePIElement):
    def __init__(
            self,
            label: str,
            uid: str,
            default_value: Optional[str] = None,
    ):
        self.label = label
        self.default_value = default_value
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"
        self.onchange = f"onchange_{self.uid}"

    def get_html_element(self) -> str:
        value = f'value="{self.default_value}"' if {self.default_value} else ""

        res = f"""
    <div class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <input class="sdpi-item-value" id="{self.uid}" type="month" {value} onchange="{self.onchange}()">
    </div>
        """
        return res

    def get_js_code(self) -> str:
        template = Template("""
    const ${onchange} = () => {
        console.log(${js_el_const}.value);
        settings["${uid}"] = ${js_el_const}.value;
        $$PI.setSettings(settings);
    }
        """)

        res = template.substitute(onchange=self.onchange, uid=self.uid, js_el_const=self.js_el_const)
        return res

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
