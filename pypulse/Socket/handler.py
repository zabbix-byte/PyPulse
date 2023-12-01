import http.server
from urllib import parse

from pypulse.Template import Template
from pypulse.View.views import get


class Request(http.server.SimpleHTTPRequestHandler):
    raw_request = None
    response = None

    def __check_request(self):
        self.__request_content()

        view = get(self.path)
        if not view:
            return False

        self.response = view[0](
            self) if not view[1] else view[0](self, **view[1])

        if type(self.response).__name__ not in ['Redirect', 'RenderTemplate', 'Reload']:
            return False
        
        return True

    def __request_content(self):
        raw_length = self.headers.get('content-length')
        if not raw_length:
            return
        length = int(raw_length)

        self.raw_request = self.rfile.read(length)

    def __return_template(self):
        if not self.response:
            return

        render, redirect = self.response.render_template(self)
        self.end_headers()
        if not redirect:
            template = ' '.join(render.splitlines())

            self.wfile.write(template.encode())

    def __handler(self):
        condition = self.__check_request()

        if not condition:
            return getattr(http.server.SimpleHTTPRequestHandler, f'do_{self.command}')(self)

        self.__return_template()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=Template.STATIC_PATH, **kwargs)

    @property
    def parameters(self):
        result = {}
        for i in parse.parse_qsl(self.raw_request):
            result[i[0].decode()] = i[1].decode()
        return result

    def do_GET(self): self.__handler()
    def do_POST(self): self.__handler()
