from string import Template
from typing import List, Optional

from .base import BasePIElement


class Range(BasePIElement):
    def __init__(
            self,
            label: str,
            uid: str,
            max_value: float = 100,
            min_value: float = 0,
            default_value: float = 0,
            step: Optional[float] = None,
            left_label: Optional[str] = None,
            right_label: Optional[str] = None,
            datalist: Optional[List[str]] = None,
    ):
        if (right_label or left_label) and datalist:
            raise ValueError("(right_label or left_label) and datalist are not supported together")

        self.step = step
        self.left_label = left_label
        self.right_label = right_label
        self.max_value = max_value
        self.min_value = min_value
        self.label = label
        self.default_value = default_value
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"
        self.onchange = f"onchange_{self.uid}"
        self.datalist = datalist

    def get_html_element(self) -> str:
        if not self.datalist:
            datalist_class = ""
            range_list = ""
            datalist = ""
            left_label = f"<span>{self.left_label}</span>" if self.left_label else ""
            right_label = f"<span>{self.right_label}</span>" if self.right_label else ""
        else:
            datalist_class = " datalist"
            datalist_id = f"{self.uid}datalist"
            range_list = f' list="{datalist_id}"'
            datalist_items = "\n".join([f'<option>{datalist_label}</option>' for datalist_label in self.datalist])
            datalist = f"""
            <datalist id="{datalist_id}">
                {datalist_items}
            </datalist>
            """
            left_label = ""
            right_label = ""

        step = f' step="{self.step}"' if self.step else ""

        res = f"""
    <div type="range" class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <div class="sdpi-item-value{datalist_class}">
            {left_label}
            <input type="range" id="{self.uid}" value="{self.default_value}" min="{self.min_value}" 
            max="{self.max_value}" {step} onchange="{self.onchange}()" {range_list}>
            {datalist}
            {right_label}
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
