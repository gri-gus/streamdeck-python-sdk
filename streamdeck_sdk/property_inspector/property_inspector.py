from pathlib import Path
from typing import List

from .objs.base import BasePIElement


class PropertyInspector:
    def __init__(
            self,
            action_uuid: str,
            elements: List["BasePIElement"],
    ):
        self.action_uuid = action_uuid
        self.action_name = self.action_uuid.split(".")[-1]
        self.elements = elements

    def build(self, output_dir: Path, template: Path):
        html_elements = "\n".join([element.get_html_element() for element in self.elements])
        html_elements = "\n".join([line for line in html_elements.splitlines() if line.strip() != ""])

        js_code = "\n".join([element.get_js_code() for element in self.elements])
        js_code = "\n".join([line for line in js_code.splitlines() if line.strip() != ""])

        html_element_js_const = "\n".join([element.get_js_consts() for element in self.elements])
        html_element_js_const = "\n".join([line for line in html_element_js_const.splitlines() if line.strip() != ""])

        on_connect_js = "\n".join([element.get_on_connect_js() for element in self.elements])
        on_connect_js = "\n".join([line for line in on_connect_js.splitlines() if line.strip() != ""])

        on_did_receive_settings_js = "\n".join([element.get_on_did_receive_settings_js() for element in self.elements])
        on_did_receive_settings_js = "\n".join(
            [line for line in on_did_receive_settings_js.splitlines() if line.strip() != ""]
        )

        with open(template, "r") as f:
            index_template_text = f.read()

        res_text = index_template_text.replace(
            "<!--    YOUR HTML CODE   -->",
            html_elements,
        )
        res_text = res_text.replace(
            "<!--    YOUR JS CODE   -->",
            js_code,
        )
        res_text = res_text.replace(
            "<!--    YOUR JS CODE CONSTS   -->",
            html_element_js_const,
        )
        res_text = res_text.replace(
            "<!--    YOUR JS CODE ON_CONNECT   -->",
            on_connect_js,
        )
        res_text = res_text.replace(
            "YOUR_ACTION_UUID",
            self.action_uuid,
        )
        res_text = res_text.replace(
            "// YOUR_ON_DID_RECEIVE_SETTINGS_JS",
            on_did_receive_settings_js
        )

        with open(output_dir / f"{self.action_name}_pi.html", "w") as f:
            f.write(res_text)
