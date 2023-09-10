import argparse

def main():
    print(
r"""
██████╗ ██╗   ██╗██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝██║   ██║██║     ███████╗█████╗  
██╔═══╝   ╚██╔╝  ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
██║        ██║   ██║     ╚██████╔╝███████╗███████║███████╗
╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
         _                      _     _     _      
        | |__  _   _   ______ _| |__ | |__ (_)_  __
        | '_ \| | | | |_  / _` | '_ \| '_ \| \ \/ /
        | |_) | |_| |  / / (_| | |_) | |_) | |>  < 
        |_.__/ \__, | /___\__,_|_.__/|_.__/|_/_/\_\
                |___/                                                                                       
"""
    )
    parser = argparse.ArgumentParser(description='PyPulse is a powerful tool designed to simplify the creation of desktop applications based on Chromium.\n Whether you\'re building custom web browsers, integrating web content into your application, or creating web-based desktop apps, PyPulse empowers you to do it efficiently and seamlessly.')
    parser.add_argument('--create_project', help='This command initializes a new project in the PyPulse application, allowing you to specify the project name, template, and other configuration options.')
    parser.add_argument('--create_app', help='The `create-app` command allows you to generate a new app within your PyPulse project.')
    args = parser.parse_args()


    print(args)

    