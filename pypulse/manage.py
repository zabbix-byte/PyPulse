import argparse
import platform
import os
import importlib.metadata
import zipfile
import shutil
from pathlib import Path

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
    print(f'v{importlib.metadata.version("python-pulse")}')
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
    print('[PyPulse] Creating project....')

    if project_name_path is None:
        raise ValueError(
            '[PyPulse] create_new_project function only accept by parameter a string')

    if os.path.isdir(project_name_path):
        print('[PyPulse] Already exists a project with the same name in this path\n')
        exit()

    if os.path.isdir('tmp-project'):
        print('[PyPulse] Already exists a temp file in project\n')
        exit()

    os.mkdir('tmp-project')

    import requests
    project_name = project_name_path.split(PATH_SEPARATOR)[-1]

    response = requests.get(
        'https://github.com/zabbix-byte/PyPulse-HelloWorld-Project/archive/refs/heads/main.zip')
    f = open(os.path.join('tmp-project', 'temp.zip'), "wb")
    f.write(response.content)
    f.close()

    with zipfile.ZipFile(os.path.join('tmp-project', 'temp.zip'), 'r') as zip_ref:
        zip_ref.extractall('tmp-project')

    shutil.copytree(os.path.join(
        'tmp-project', 'PyPulse-HelloWorld-Project-main'), project_name_path)
    shutil.rmtree('tmp-project')

    ### Changing names
    path_to_project_old_name = os.path.join(project_name_path, 'HelloWorld.py')
    os.rename(path_to_project_old_name, os.path.join(project_name_path, f'{project_name_path}.py'))

    ### Repvomg files

    os.remove(os.path.join(project_name_path, 'README.md'))
    os.remove(os.path.join(project_name_path, '.gitignore'))


    print(f'[PyPulse] Project with name {project_name} has been created!\n')
