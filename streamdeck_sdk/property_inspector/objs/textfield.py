from string import Template

from .base import BasePIElement


class Textfield(BasePIElement):
    def __init__(
            self,
            label: str,
            uid: str,
            required: bool = False,
            pattern: str = "",
            placeholder: str = "",
            default_value: str = "",
    ):
        self.label = label
        self.placeholder = placeholder
        self.required = required
        self.pattern = pattern
        self.default_value = default_value
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"
        self.onchange = f"onchange_{self.uid}"

    def get_html_element(self) -> str:
        required = "required" if self.required else ""
        pattern = f'pattern="{self.pattern}"' if self.pattern else ""

        res = f"""
    <div class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <input class="sdpi-item-value" id="{self.uid}" {required} type="text" onchange="{self.onchange}()"
               value="{self.default_value}" placeholder="{self.placeholder}" {pattern}>
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
