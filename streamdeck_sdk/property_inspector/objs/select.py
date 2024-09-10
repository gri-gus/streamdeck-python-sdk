from string import Template
from typing import List, Optional

from .base import BasePIElement


def remove_duplicates(strings):
    seen = set()
    result = []
    for string in strings:
        if string not in seen:
            seen.add(string)
            result.append(string)
    return result


class Select(BasePIElement):
    def __init__(
            self,
            uid: str,
            label: str,
            values: List[str],
            default_value: Optional[str] = None,
    ):
        """
        The value in the settings will look like: [["element 1", "element 2", ...], "selected element"]
        """
        self.label = label
        if default_value is not None and default_value not in values:
            raise ValueError("default_value not in values")
        self.values = remove_duplicates(values)
        self.default_value = default_value
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"
        self.onchange = f"onchange_{self.uid}"

    def get_html_element(self) -> str:
        default_exists = False
        options = []
        for value in self.values:
            if value == self.default_value:
                default_exists = True
                option = f'<option selected value="{value}">{value}</option>'
            else:
                option = f'<option value="{value}">{value}</option>'
            options.append(option)
        if default_exists:
            null_option = '<option value="null"></option>'
        else:
            null_option = '<option selected value="null"></option>'

        options = "\n".join([null_option, *options])
        res = f"""
    <div class="sdpi-item">
        <div class="sdpi-item-label">{self.label}</div>
        <select class="sdpi-item-value select" id="{self.uid}" onchange="{self.onchange}()">
            {options}
        </select>
    </div>
        """
        return res

    def get_js_code(self) -> str:
        template = Template("""
    const ${onchange} = () => {
        console.log(${js_el_const}.value);
        let values_and_selected = get_select_values_and_selected(
            ${js_el_const},
        )
        settings["${uid}"] = [
            values_and_selected.values,
            values_and_selected.selected,
        ]
        $$PI.setSettings(settings);
    }
        """)

        res = template.substitute(onchange=self.onchange, uid=self.uid, js_el_const=self.js_el_const)
        return res

    def get_on_connect_js(self) -> str:
        template = Template("""
        if (settings["${uid}"] !== undefined) {
            let update_result = update_select_options(
                ${js_el_const},
                settings["${uid}"][0],
                settings["${uid}"][1],
            )
            if (!update_result) {
                let values_and_selected = get_select_values_and_selected(
                    ${js_el_const},
                )
                settings["${uid}"] = [
                    values_and_selected.values,
                    values_and_selected.selected,
                ]
            }
        } else {
            let values_and_selected = get_select_values_and_selected(
                ${js_el_const},
            )
            settings["${uid}"] = [
                values_and_selected.values,
                values_and_selected.selected,
            ]
        }
        """)
        res = template.substitute(uid=self.uid, js_el_const=self.js_el_const)
        return res

    def get_js_consts(self) -> str:
        res = f"""
    const {self.js_el_const} = document.getElementById("{self.uid}")
        """
        return res
