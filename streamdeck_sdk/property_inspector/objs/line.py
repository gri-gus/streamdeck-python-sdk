from .base import BasePIElement


class Line(BasePIElement):
    def get_html_element(self) -> str:
        res = "<hr>"
        return res
