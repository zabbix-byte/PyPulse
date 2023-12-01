import os

from pypulse.Aplication.vars import Vars
from pypulse.Utils.get_apps import applications
from pypulse.Utils.routing import is_variable, variable_info
from pypulse.View.modules import filter_views, modules
from pypulse.View.types import int_logic

ROUTE_TYPES = {
    'INT': int_logic,
    'STR': str
}


def get(route: str) -> tuple:
    apps = applications()
    for app in apps:
        __modules = modules(Vars.APLICATION_PATH +
                            os.sep + app + os.sep + 'views')
        for module in __modules:
            views = filter_views(module)
            for view in views:
                keyargs = {}

                splitted_path = route.split('/')
                if splitted_path[0] == '':
                    del splitted_path[0]

                splitted_view_route = view.route.split('/')
                if splitted_view_route[0] == '':
                    del splitted_view_route[0]

                for i in range(len(splitted_view_route)):
                    if not is_variable(splitted_view_route[i]):
                        continue

                    if len(splitted_view_route) != len(splitted_path):
                        continue

                    type, name = variable_info(splitted_view_route[i])
                    assert type.upper(
                    ) in ROUTE_TYPES, f'Error at path `{view.route}`, `{type}` does not exists.'

                    value = splitted_path[i]
                    value = ROUTE_TYPES[type.upper()](value)
                    keyargs[name] = value

                    splitted_view_route[i] = splitted_path[i]

                if splitted_view_route == splitted_path:
                    return view, keyargs

                if view.route != route:
                    continue

                return view, None