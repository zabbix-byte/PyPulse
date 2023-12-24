from pypulse.Aplication.vars import Vars
from pypulse.View.views import get


class Redirect():
    def __init__(self, path: str) -> None:
        self.path = path

    def render_template(self, request):
        if self.path == request.path or get(request.path) == self.path:
            print(
                f'You tried to redirect to `{self.path}`, route that you are already in.')
            print(f'If you want to reload the current view, use `Reload`.')
            exit(1)

        request.send_response(302)
        request.send_header(
            'Location', self.path)
        return None, True
