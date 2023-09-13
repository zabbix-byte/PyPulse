from jinja2 import Environment, FileSystemLoader
from .template import Template


class RenderTemplate():
    def __init__(self, template_route: str, variables_dict: dict = None) -> None:
        self.template_route = template_route
        self.variables_dict = variables_dict

        self.envirenemnt = Environment(
            loader=FileSystemLoader(Template.TEMPLATE_PATH))

    def render_template(self):
        template = self.envirenemnt.get_template(self.template_route)
        if self.variables_dict is not None:
            output = template.render(self.variables_dict)
        else:
            output = template.render()
        return output
