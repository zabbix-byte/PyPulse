import ast


def execute_ast_view_request(request: str, node_body: object) -> None:
    import_code = ast.ImportFrom(
        module="pypulse.View",
        names=[ast.alias(name="view", asname=None)],
        level=0
    )

    import_code.lineno = 1
    import_code.col_offset = 0

    module_body = [
        import_code,
        node_body
    ]

    object_view = ast.Module(
        body=module_body, type_ignores=[])

    namespace = {
    }

    object_view = exec(
        compile(object_view, f'{node_body.name}_view', 'exec'),
        namespace
    )

    return namespace[node_body.name](request)
