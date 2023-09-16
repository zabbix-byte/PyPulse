from .view import View


class CallView:
    def __init__(self, path_to_find: str) -> None:
        self.name = None
        self.view = None
        self.requirement_view = None
        self.path_trigger = None
        self.variables_list = {}

        path_to_find = path_to_find.split('/')

        for i in View.instances:
            path = i.path_trigger.split('/')

            if len(path) != len(path_to_find):
                continue

            path_contain_variable = False
            index = []
            variables_for_index = {}

            for j in path:
                if len(j) > 0:
                    path_variable_parameters = self.find_if_variable_in_path(j)
                    if path_variable_parameters[0] != False:
                        path_contain_variable = True

                        variables_for_index[j] = (
                            path_variable_parameters[2], path_variable_parameters[1])
                        index.append(j)

            # infind the variable and his context call
            if path_contain_variable:
                # this is the part wee dont check at moment
                view_finded = True

                for path_view in range(len(path)):
                    # excluding the variables
                    element_finded = False
                    for elements_in_path in index:
                        if path.index(elements_in_path) == path_view:
                            element_finded = True
                            break

                    if element_finded:
                        continue

                    if path[path_view] != path_to_find[path_view]:
                        view_finded = False

                if view_finded:
                    self.name = i.name
                    self.view = i.view
                    self.requirement_view = i.requirement_view
                    self.path_trigger = i.path_trigger

                    for current_index_path_variable in index:
                        self.variables_list[variables_for_index[current_index_path_variable][0]] = self.parse_varible(
                            path_to_find[path.index(current_index_path_variable)], variables_for_index[current_index_path_variable][1])

                    break

            if path_contain_variable == False:
                if path == path_to_find:
                    self.name = i.name
                    self.view = i.view
                    self.requirement_view = i.requirement_view
                    self.path_trigger = i.path_trigger
                    break

    def find_if_variable_in_path(self, current_path_element: str):
        # works whit: int, str, float

        methods_allowed = ['str', 'int', 'float']

        if '<' != current_path_element[0] and '>' != current_path_element[-1]:
            return (False, )

        if ':' not in current_path_element:
            raise ValueError(
                f'The parameter you are setting in the path {current_path_element} are incorrect formated')

        type_of_var, var_name = current_path_element[1:-1].split(':')

        if type_of_var.lower() not in methods_allowed:
            raise TypeError(
                f'The type you are passing in the path {current_path_element} are not in the list of allowed var types {methods_allowed}')

        return (True, type_of_var, var_name)

    def parse_varible(self, variable: str, type_var: str):
        if type_var.lower() == 'str':
            return str(variable)

        if type_var.lower() == 'int':
            return int(variable)

        if type_var.lower() == 'float':
            return float(variable)
