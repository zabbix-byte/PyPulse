import http.server

from pypulse import View
from pypulse.Template import Template
from pypulse.Utils import execute_ast_view_request


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=Template.STATIC_PATH, **kwargs)


    def do_GET(self):
        current_view = View.CallView(self.path)
        if current_view.name is not None:
            render = execute_ast_view_request(
                node_body=current_view.view, request="eduardo", requirement_view=current_view.requirement_view)
            template = str.join(" ", render.render_template().splitlines())
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode())
        else:
            super().do_GET()
