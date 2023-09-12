import ast


def execute_ast_view_request(request: str, node_body: object) -> None:
    import_pypulse = ast.ImportFrom(
        module="pypulse.View",
        names=[ast.alias(name="view", asname=None)],
        level=0
    )

    import_pypulse.lineno = 1
    import_pypulse.col_offset = 0

    import_rendertemplate = ast.ImportFrom(
        module="pypulse.Template",
        names=[ast.alias(name="RenderTemplate", asname=None)],
        level=0
    )

    import_rendertemplate.lineno = 1
    import_rendertemplate.col_offset = 0

    module_body = [
        import_pypulse,
        import_rendertemplate,
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
