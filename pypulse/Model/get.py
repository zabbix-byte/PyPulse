
import json

from .utils import get_all_property_model, get_instance_property_value, get_meta
from pypulse.Controller import BackendInstance


class View:
    def __init__(self, model: object) -> None:
        self.__model = model
        self.model_properties = get_instance_property_value(self.__model, get_all_property_model(self.__model))
        self.model_meta = get_meta(self.__model)

    def __parse_data(self, data):
        for i in range(len(data)):
            for properties in self.model_properties:
                data[i][properties] = self.model_properties[properties].parse(data[i][properties])
        return data

    def all(self):
        data = BackendInstance.instance.get_data(self.model_meta.target)

        try:
            data = json.loads(data)
        except:
            return data

        if type(data) is not list:
            data = [data]

        return self.__parse_data(data)

    @FutureWarning
    def filter(self, **kwargs):
        data = BackendInstance.instance.get_data(self.model_meta.target)

        try:
            data = json.loads(data)
        except:
            return data

        if type(data) is not list:
            data = [data]

        return self.__parse_data(data)
