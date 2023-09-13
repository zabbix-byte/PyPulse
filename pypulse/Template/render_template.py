from jinja2 import Environment, FileSystemLoader
from pypulse.Window.load_browser import LoadBrowser
from .template import Template


class RenderTemplate():
    def __init__(self, template_route: str, variables_dict: dict) -> None:
        self.template_route = template_route
        self.variables_dict = variables_dict

        self.envirenemnt = Environment(
            loader=FileSystemLoader(Template.template_path))

    def render_template(self):
        template = self.envirenemnt.get_template(self.template_route)
        output = template.render(self.variables_dict)
        return output
