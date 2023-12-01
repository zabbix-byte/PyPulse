import importlib
import inspect
import os

from pypulse.Aplication.vars import Vars


def filter_files(extension: str, files: str):
    filtered = []
    for file in files:
        if not file.endswith('.' + extension):
            continue
        filtered.append(file)

    return filtered


def modules(folder: str) -> list:
    files: list[str] = [f'{folder}' + os.sep + file
                        # add as suffix the folder
                        for file in filter_files('py', os.listdir(folder))]

    modules: list = []
    for file in files:
        separate_folder = file.split('\\')
        separate_folder[-1] = separate_folder[-1].rsplit('.', 1)[0]
        name = '.'.join(separate_folder)

        spec = importlib.util.spec_from_file_location(name, file)
        view_module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(view_module)
        modules.append(view_module)

    return modules


def filter_views(module) -> list:
    attributes = dir(module)
    views = []
    for attr_name in attributes:
        attr = getattr(module, attr_name)

        if not inspect.isfunction(attr):
            continue

        if attr.__name__ in globals():
            continue

        if attr.__name__ not in Vars.VIEWS:
            continue

        views.append(attr)

    return views
