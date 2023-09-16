import ast


def execute_ast_view_request(request: str, node_body: object, requirement_view: list, other_variables: dict = {}) -> None:
    module_body = []

    for i in requirement_view:
        import_q = i[0]
        import_as_name = i[1]

        if '.' in import_q:
            current_path = import_q.rsplit('.', 1)
            import_lib = ast.ImportFrom(
                module=current_path[0],
                names=[ast.alias(name=current_path[1], asname=import_as_name)],
                level=0
            )
        else:
            import_lib = ast.Import(
                names=[ast.alias(name=import_q, asname=import_as_name)])

        import_lib.lineno = 1
        import_lib.col_offset = 0
        module_body.append(import_lib)

    module_body.append(node_body)

    object_view = ast.Module(
        body=module_body, type_ignores=[])

    namespace = {}

    object_view = exec(
        compile(object_view, f'{node_body.name}_view', 'exec'),
        namespace
    )

    variables = {
        'request': request
    }

    variables.update(other_variables)

    return namespace[node_body.name](**variables)
