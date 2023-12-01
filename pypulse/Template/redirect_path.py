from pypulse.View import CallView
from pypulse.Utils import execute_ast_view_request


class Redirect():
    def __init__(self, path: str) -> None:
        self.view = CallView(path)

    def get_render(self, request):
        render = execute_ast_view_request(
            node_body=self.view.view, request=request, requirement_view=self.view.requirement_view)

        if type(render).__name__ == 'Redirect':
            raise RecursionError('You cant do a recursive redirect!')

        return render
