from string import Template
from typing import List

from .base import BasePIElement, BaseElement


class RadioItem(BaseElement):
    def __init__(
            self,
            value: str,
            label: str = "",
            checked: bool = False,
    ):
        self.label = label
        self.checked = checked
        self.value = value

    def get_html_element(self, uid: str, name: str) -> str:
        checked = "checked" if self.checked else ""
        label = self.label if self.label else ""

        res = f"""
            <span class="sdpi-item-child">
                <input id="{uid}" type="radio" name="{name}"
                    value="{self.value}" {checked} >
                <label for="{uid}" class="sdpi-item-label">
                    <span></span>{label}
                </label>
            </span>
        """
        return res


class Radio(BasePIElement):
    def __init__(
            self,
            label: str,
            uid: str,
            items: List[RadioItem],
    ):
        self.label = label
        self.items = items
        self.uid = uid

    def get_html_element(self) -> str:
        item_html_elements = []
        for index, item in enumerate(self.items):
            item_uid = f"{self.uid}_item_{index}"
            item_html_element = item.get_html_element(uid=item_uid, name=self.uid)
            item_html_elements.append(item_html_element)
        items = "\n".join(item_html_elements)

        res = f"""
    <div type="radio" class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <div class="sdpi-item-value">
            {items}
        </div>
    </div>
        """

        return res

    def get_js_code(self) -> str:
        template = Template("""
    document.addEventListener('input',(e)=>{
        if(e.target.getAttribute('name')==="${uid}") {
    console.log(e.target.name, e.target.value)
    settings["${uid}"] = e.target.value
    $$PI.setSettings(settings);}
    })
        """)
        res = template.substitute(uid=self.uid)
        return res

    def get_on_connect_js(self) -> str:
        template = Template("""
        let ${uid}_el;
        if (settings["${uid}"] !== undefined) {
            ${uid}_el = document.querySelector(`input[type="radio"][name="${uid}"][value="$${settings.${uid}}"]`)
            ${uid}_el.checked = true
        } else {
            ${uid}_el = document.querySelector('input[type="radio"][name="${uid}"]:checked')
            settings["${uid}"] = ${uid}_el.value
        }
        """)
        res = template.substitute(uid=self.uid)
        return res

    def get_js_consts(self) -> str:
        return ""
