from .utils import get_all_property_model, get_instance_property_value, get_meta
from pypulse.Controller import BackendInstance


class View:
    def __init__(self, model: object) -> None:
        self.__model = model
        self.model_properties = get_instance_property_value(
            self.__model, get_all_property_model(self.__model)
        )
        self.model_meta = get_meta(self.__model)

    def __parse_data(self, data):
        properties = [properties for properties in self.model_properties]

        data = [
            {key: value for key, value in d.items() if key in properties} for d in data
        ]

        for i in range(len(data)):
            for properties in self.model_properties:
                data[i][properties] = self.model_properties[properties].parse(
                    data[i][properties]
                )

        return data

    def all(self):
        if "method" in dir(self.model_meta):
            method = self.model_meta.method

        if method.lower() == "get":
            data = BackendInstance.instance.get_data(self.model_meta.target)
        elif method.lower() == "post":
            body = {}

            if "body" in dir(self.model_meta):
                body = self.model_meta.body
                self.__model.Meta.body = None

            data = BackendInstance.instance.post_data(
                endpoint=self.model_meta.target, body=body
            )

        else:
            data = BackendInstance.instance.get_data(self.model_meta.target)

        if type(data) is int:
            return data

        if type(data) is not list:
            data = [data]

        return self.__parse_data(data)

    @FutureWarning
    def filter(self, **kwargs):
        pass
