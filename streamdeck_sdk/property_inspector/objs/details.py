from string import Template
from typing import Optional

from .base import BasePIElement


class Details(BasePIElement):
    def __init__(
            self,
            uid: str,
            label: str = "",
            text: str = "",
            heading: Optional[str] = None,
            full_width: bool = False,
            default_open: bool = False,
    ):
        self.heading = heading
        self.text = text
        self.default_open = default_open
        self.full_width = full_width
        self.label = label
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"

    def get_html_element(self) -> str:
        default_open = f'open' if self.default_open else ""
        if self.label:
            label = f'<div class="sdpi-item-label">{self.label}</div>'
        elif not self.full_width:
            label = f'<div class="sdpi-item-label empty"></div>'
        else:
            label = ""
        text = "\n".join([f"<p>{line.strip()}</p>" for line in self.text.splitlines() if line.strip()])
        heading = f'<summary>{self.heading}</summary>' if self.heading else ""

        res = f"""
    <div class="sdpi-item details">
        {label}
        <details class="sdpi-item-value" {default_open}>
            {heading}
            <div id="{self.uid}">{text}</div>
        </details>
    </div>
        """
        return res

    def get_on_connect_js(self) -> str:
        template = Template(r"""
         if (settings["${uid}"] !== undefined) {
             ${js_el_const}.innerHTML = settings.${uid}
                 .split('\n')
                 .map(line => line.trim())
                 .filter(line => line)
                 .map(line => `<p>$${line}</p>`)
                 .join('\n');
         } else {
             settings["${uid}"] = ${js_el_const}.textContent;
         }
         """)
        res = template.substitute(uid=self.uid, js_el_const=self.js_el_const)
        return res

    def get_js_consts(self) -> str:
        res = f"""
     const {self.js_el_const} = document.getElementById("{self.uid}")
         """
        return res
