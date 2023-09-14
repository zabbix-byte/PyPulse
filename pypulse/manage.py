import argparse
import platform
import os
import importlib.metadata

MANAGE_lOGO = r"""
██████╗ ██╗   ██╗██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝██║   ██║██║     ███████╗█████╗  
██╔═══╝   ╚██╔╝  ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
██║        ██║   ██║     ╚██████╔╝███████╗███████║███████╗
╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝                                                                                
"""

PATH_SEPARATOR = '/' if platform.system() == 'Linux' else '\\'


def main():
    print(f'v{importlib.metadata.version("pypulse")}')
    print(MANAGE_lOGO)

    parser = argparse.ArgumentParser(
        description='PyPulse is a powerful tool designed to simplify the creation of desktop applications based on Chromium.\n Whether you\'re building custom web browsers, integrating web content into your application, or creating web-based desktop apps, PyPulse empowers you to do it efficiently and seamlessly.')
    parser.add_argument(
        '--create_project', help='This command initializes a new project in the PyPulse application, allowing you to specify the project name, template, and other configuration options.')
    parser.add_argument(
        '--create_app', help='The `create-app` command allows you to generate a new app within your PyPulse project.')

    args = parser.parse_args()

    if args.create_project:
        create_new_project(args.create_project)


def create_new_project(project_name_path: str):
    if project_name_path is None:
        raise ValueError(
            '[PyPulse] create_new_project function only accept by parameter a string')

    if not os.path.isdir(project_name_path):
        os.mkdir(project_name_path)
    else:
        print('[PyPulse] Already exists a project with the same name in this path\n')
        exit()

    import requests
    project_name = project_name_path.split(PATH_SEPARATOR)[-1]

    response = requests.get('https://github.com/zabbix-byte/PyPulse/archive/refs/heads/main.zip')
    open(f'{project_name_path}.zip', "wb").write(response.content)


    print(f'[PyPulse] Project with name {project_name} has been created!\n')
