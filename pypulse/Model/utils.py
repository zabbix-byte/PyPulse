def get_all_property_model(cls: object) -> list:
    return [property for property in dir(cls) if '__' != property[0:2] and property not in ['view', 'Meta', 'body']]


def get_instance_property_value(cls: object, properties: list) -> dict:
    result = {}

    for property in properties:
        result[property] = getattr(cls, property)

    return result


def get_meta(cls: object) -> object:
    return getattr(cls, 'Meta')
