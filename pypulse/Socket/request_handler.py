import http.server

from pypulse import Aplication, View
from pypulse.Utils import execute_ast_view_request


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        current_view = View.CallView(self.path)
        if current_view.name is not None:
            render = execute_ast_view_request(
                node_body=current_view.view, request="eduardo")
            template = str.join(" ", render.render_template().splitlines())
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode())
        else:
            super().do_GET()
