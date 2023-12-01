import os
import ast

from .vars import Vars
from pypulse import View


def get_imports(node):
    imports = []
    for item in node.body:
        if isinstance(item, ast.Import):
            for alias in item.names:
                imports.append((alias.name, alias.asname))

        elif isinstance(item, ast.ImportFrom):
            module = item.module
            for alias in item.names:
                imports.append((f"{module}.{alias.name}", alias.asname))
    return imports


class ReadViews:
    @staticmethod
    def find_views_ho_are_using_the_decoratos(aplication_dir: str):

        complete_route_path = os.path.join(
            Vars.APLICATION_PATH, aplication_dir)

        dirs_module = []

        for path, subdirs, files in os.walk(complete_route_path):
            if '__pycache__' in path:
                continue
            for name in files:
                dirs_module.append(os.path.join(path, name))

        for file in dirs_module:
            with open(file, 'r') as file:
                file_contents = file.read()

            # Parse the file's content into an Abstract Syntax Tree (AST)
            parsed_ast = ast.parse(file_contents)

            target_decorator = "@view"

            all_imports = get_imports(parsed_ast)

            for node in ast.walk(parsed_ast):
                if isinstance(node, ast.FunctionDef):

                    for decorator in node.decorator_list:
                        if isinstance(decorator, ast.Call) and decorator.func.id == target_decorator.lstrip("@"):
                            current_name = None
                            current_path_trigger = None

                            for keyword in decorator.keywords:
                                if keyword.arg == "name":
                                    current_name = ast.dump(keyword.value).split(
                                        "value='")[-1].split("'")[0]
                                elif keyword.arg == "path_trigger":
                                    current_path_trigger = ast.dump(
                                        keyword.value).split("value='")[-1].split("'")[0]

                                if current_name is not None and current_path_trigger is not None:
                                    break

                            View.SetView(
                                f'{aplication_dir}___{current_name}',
                                node,
                                all_imports,
                                current_path_trigger
                            )
