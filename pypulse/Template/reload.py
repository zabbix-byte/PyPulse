from pypulse.Aplication.vars import Vars
from pypulse.View.views import get


class Reload:

    def __init__(self) -> None:
        pass

    def render_template(self, request):
        view = get(request.path)
        request.command = 'GET'
        response = view[0](request) if not view[1] else view[0](
            request, **view[1])
        if type(response).__name__ == 'Reload':
            print(
                f'Path `{request.path}` returns reload in a loop (infinite recursion).')
            exit(1)

        request.send_response(302)
        request.send_header(
            'Location', request.path)
        return None, True
