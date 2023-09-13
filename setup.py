from setuptools import find_packages, setup

setup(
    name='pypulse',
    packages=find_packages(),
    version='no_release',
    description='',
    author='zabbix-byte',
    license='MIT',
    test_suite="tests",
    install_reqs = ['cefpython3==66.1', 'Jinja2==3.1.2', 'wxPython==4.2.1'],
    entry_points={
        'console_scripts': [
            'pypulse-manage = pypulse.manage:main'
        ]
    },
)