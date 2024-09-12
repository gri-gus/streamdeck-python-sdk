from .base import BasePIElement


class Heading(BasePIElement):
    def __init__(
            self,
            label: str,
    ):
        self.label = label

    def get_html_element(self) -> str:
        res = f"""
    <div class="sdpi-heading">{self.label}</div>
        """
        return res
