from __future__ import annotations

import json
from typing import TYPE_CHECKING, Union

from jinja2 import Environment, FileSystemLoader

from .template import Template

if TYPE_CHECKING:
    from ..Socket.handler import Request


class RenderTemplate:
    
    def __init__(self, template_route: str, variables_dict: dict = None):
        self.template_route: str = template_route
        self.variables_dict: dict = variables_dict

        self.jinja_env: Environment = Environment(loader=FileSystemLoader(Template.TEMPLATE_PATH))

    def render_template(self, request: Request) -> Union[str, bool]:
        request.send_response(200)
        request.send_header('Content-Type', 'text/html')

        jinja_template = self.jinja_env.get_template(self.template_route)
        
        if self.variables_dict is not None:
            return jinja_template.render(self.variables_dict), False

        return jinja_template.render(), False


class RenderJson:

    def __init__(self, json_to_render: Union[dict, list]):
        self.json_to_render: Union[dict, list] = json_to_render

    def render_template(self, request: Request) -> Union[str, bool]:
        request.send_response(200)
        request.send_header('Content-Type', 'application/json')

        return json.dumps(self.json_to_render), False
