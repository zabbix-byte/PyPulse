import http.server

from pypulse import View
from pypulse.Template import Template
from pypulse.Utils import execute_ast_view_request
import urllib.parse

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=Template.STATIC_PATH, **kwargs)

    def do_GET(self):
        current_view = View.CallView(self.path)
        if current_view.name is not None:
            request = {
                'method': 'GET',
                'headers': {
                    'Host': self.headers.get('Host'),
                    'Upgrade-Insecure-Requests': self.headers.get('Upgrade-Insecure-Requests'),
                    'User-Agent': self.headers.get('User-Agent'),
                    'Accept': self.headers.get('Accept'),
                    'Accept-Encoding': self.headers.get('Accept-Encoding'),
                    'Accept-Language': self.headers.get('Accept-Language')
                }
            }

            render = execute_ast_view_request(
                node_body=current_view.view, request=request, requirement_view=current_view.requirement_view, other_variables=current_view.variables_list)

            if type(render).__name__ == 'Redirect':
                render = render.get_render(request)

            template = str.join(" ", render.render_template().splitlines())
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode())
        else:
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = urllib.parse.parse_qs(self.rfile.read(content_length).decode('utf-8'))
        temp_post_body = {}

        for i in post_body:
            temp_post_body[i] = post_body[i][0]

        current_view = View.CallView(self.path)

        if current_view.name is not None:
            request = {
                'method': 'POST',
                'headers': {
                    'Host': self.headers.get('Host'),
                    'Upgrade-Insecure-Requests': self.headers.get('Upgrade-Insecure-Requests'),
                    'User-Agent': self.headers.get('User-Agent'),
                    'Accept': self.headers.get('Accept'),
                    'Accept-Encoding': self.headers.get('Accept-Encoding'),
                    'Accept-Language': self.headers.get('Accept-Language')
                },
                'body': temp_post_body
            }

            render = execute_ast_view_request(
                node_body=current_view.view, request=request, requirement_view=current_view.requirement_view)

            if type(render).__name__ == 'Redirect':
                render = render.get_render(request)

            template = str.join(" ", render.render_template().splitlines())
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode())
        else:
            super().do_POST()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        temp_post_body = {}
        for i in post_body.decode('utf-8').split('&'):
            element = i.split('=')
            if len(element) == 2:
                temp_post_body[element[0]] = element[1]

        current_view = View.CallView(self.path)

        if current_view.name is not None:
            request = {
                'method': 'PUT',
                'headers': {
                    'Host': self.headers.get('Host'),
                    'Upgrade-Insecure-Requests': self.headers.get('Upgrade-Insecure-Requests'),
                    'User-Agent': self.headers.get('User-Agent'),
                    'Accept': self.headers.get('Accept'),
                    'Accept-Encoding': self.headers.get('Accept-Encoding'),
                    'Accept-Language': self.headers.get('Accept-Language')
                },
                'body': temp_post_body
            }

            render = execute_ast_view_request(
                node_body=current_view.view, request=request, requirement_view=current_view.requirement_view)

            if type(render).__name__ == 'Redirect':
                render = render.get_render(request)

            template = str.join(" ", render.render_template().splitlines())
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode())
        else:
            super().do_PUT()

    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        temp_post_body = {}
        for i in post_body.decode('utf-8').split('&'):
            element = i.split('=')
            if len(element) == 2:
                temp_post_body[element[0]] = element[1]

        current_view = View.CallView(self.path)

        if current_view.name is not None:
            request = {
                'method': 'PATCH',
                'headers': {
                    'Host': self.headers.get('Host'),
                    'Upgrade-Insecure-Requests': self.headers.get('Upgrade-Insecure-Requests'),
                    'User-Agent': self.headers.get('User-Agent'),
                    'Accept': self.headers.get('Accept'),
                    'Accept-Encoding': self.headers.get('Accept-Encoding'),
                    'Accept-Language': self.headers.get('Accept-Language')
                },
                'body': temp_post_body
            }

            render = execute_ast_view_request(
                node_body=current_view.view, request=request, requirement_view=current_view.requirement_view)

            if type(render).__name__ == 'Redirect':
                render = render.get_render(request)

            template = str.join(" ", render.render_template().splitlines())
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(template.encode())
        else:
            super().do_PATCH()
