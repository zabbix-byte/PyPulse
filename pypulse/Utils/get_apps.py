import os

from pypulse.Aplication.aplication import Aplication
from pypulse.Aplication.vars import Vars


def get_folders(path: str):
    dir = os.listdir(path)
    result = []

    for i in dir:
        if not os.path.isdir(path + "\\" + i):
            continue

        result.append(i)

    return result


def applications():
    folder = get_folders(Vars.APLICATION_PATH)
    apps = []

    for i in folder:
        if not i:
            continue

        if i not in [j.name for j in Aplication.instances]:
            continue

        apps.append(i)

    return apps
