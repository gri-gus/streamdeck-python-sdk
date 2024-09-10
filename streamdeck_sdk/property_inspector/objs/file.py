from string import Template
from typing import List, Optional

from .base import BasePIElement


class File(BasePIElement):
    def __init__(
            self,
            label: str,
            uid: str,
            accept: Optional[List[str]] = None,
            placeholder: str = "no file...",
    ):
        if accept:
            self.accept = ", ".join(accept)
        else:
            self.accept = None
        self.label = label
        self.placeholder = placeholder
        self.uid = uid
        self.uid_label = f"{self.uid}_label"
        self.js_el_const = f"{self.uid}_el"
        self.js_el_label_const = f"{self.uid_label}_el"
        self.onchange = f"onchange_{self.uid}"

    def get_html_element(self) -> str:
        accept = f'accept="{self.accept}"' if self.accept else ""

        res = f"""
    <div class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <div class="sdpi-item-group file">
            <input class="sdpi-item-value" id="{self.uid}" type="file" {accept} onchange="{self.onchange}()">
            <label class="sdpi-file-info" id="{self.uid_label}" for="{self.uid}"
                   style="overflow-y: auto; min-width: 135px; max-width: 135px; max-height: 40px">
                   {self.placeholder}
           </label>
            <label class="sdpi-file-label" for="{self.uid}">Choose file...</label>
        </div>
    </div>
        """
        return res

    def get_js_code(self) -> str:
        template = Template(r"""
    function ${onchange}() {
        if (${js_el_const}.type !== "file") {
            return
        }
        let result = decodeURIComponent(${js_el_const}.value.replace(/^C:\\fakepath\\/, ''));
        console.log(result)
        if (result) {
            ${js_el_label_const}.textContent = result;
            settings["${uid}"] = result;
        } else {
            ${js_el_label_const}.textContent = "${placeholder}";
            settings["${uid}"] = null;
        }
        $$PI.setSettings(settings)
    }
        """)

        res = template.substitute(
            uid=self.uid,
            js_el_const=self.js_el_const,
            js_el_label_const=self.js_el_label_const,
            onchange=self.onchange,
            placeholder=self.placeholder,
        )
        return res

    def get_on_connect_js(self) -> str:
        template = Template("""
        if (settings["${uid}"] !== undefined) {
            if (settings.${uid}) {
                ${js_el_label_const}.textContent = settings.${uid};   
            } else {
                ${js_el_label_const}.textContent = "${placeholder}";
            }
        } else {
            ${js_el_label_const}.textContent = "${placeholder}";
            settings["${uid}"] = null;
        }
        """)
        res = template.substitute(
            uid=self.uid,
            js_el_label_const=self.js_el_label_const,
            placeholder=self.placeholder,
        )

        return res

    def get_js_consts(self) -> str:
        res = f"""
    const {self.js_el_const} = document.getElementById("{self.uid}")
    const {self.js_el_label_const} = document.getElementById("{self.uid_label}")
        """
        return res
