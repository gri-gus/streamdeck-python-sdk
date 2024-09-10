from string import Template
from typing import Optional

from .base import BasePIElement


class Textarea(BasePIElement):
    def __init__(
            self,
            label: str,
            uid: str,
            max_length: Optional[int] = None,
            placeholder: str = "",
            info_text: str = "",
    ):
        self.max_length = max_length
        self.label = label
        self.placeholder = placeholder
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"
        self.onchange = f"onchange_{self.uid}"
        self.info_text = info_text

    def get_html_element(self) -> str:
        max_length = f'maxlength="{self.max_length}"' if self.max_length is not None else ""

        res = f"""
    <div type="textarea" class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <div class="sdpi-item-value textarea">
        <textarea type="textarea" {max_length} id="{self.uid}" 
            placeholder="{self.placeholder}" onchange="{self.onchange}()"></textarea>
        <label for="{self.uid}">{self.info_text}</label>
        </div>
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
