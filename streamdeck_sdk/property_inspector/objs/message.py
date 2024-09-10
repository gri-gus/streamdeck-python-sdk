from enum import Enum
from string import Template

from .base import BasePIElement


class MessageTypes(Enum):
    INFO = "info"
    CAUTION = "caution"
    QUESTION = "question"
    NONE = ""


class Message(BasePIElement):
    def __init__(
            self,
            uid: str,
            heading: str,
            text: str = "",
            message_type: MessageTypes = MessageTypes.INFO,
            default_open: bool = False,
    ):
        self.heading = heading
        self.text = text
        self.message_type = message_type
        self.default_open = default_open
        self.uid = uid
        self.js_el_const = f"{self.uid}_el"

    def get_html_element(self) -> str:
        default_open = f'open' if self.default_open else ""
        text = "\n".join([f"<p>{line.strip()}</p>" for line in self.text.splitlines() if line.strip()])

        res = f"""
        <div class="sdpi-item">
            <details class="message {self.message_type.value}" {default_open}>
                <summary>{self.heading}</summary>
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
