import os
import ast

from .vars import Vars

class ReadViews:
    @staticmethod
    def find_views_ho_are_using_the_decoratos(aplication_dir: str):

        complete_route_path = os.path.join(Vars.APLICATION_PATH, aplication_dir)

        for i in os.listdir(complete_route_path):
            with open(f'{complete_route_path}\{i}', 'r') as file:
                file_contents = file.read()

            # Parse the file's content into an Abstract Syntax Tree (AST)
            parsed_ast = ast.parse(file_contents)

            target_decorator = "@PathView"

            for node in ast.walk(parsed_ast):
                if isinstance(node, ast.FunctionDef):
                    for decorator in node.decorator_list:
                        if isinstance(decorator, ast.Call) and decorator.func.id == target_decorator.lstrip("@"):
                            code = compile(node, filename='blah', mode='exec')


                            


