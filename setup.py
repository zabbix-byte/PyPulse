from setuptools import find_packages, setup

setup(
    name='pypulse',
    packages=find_packages(),
    version='0.1',
    description='',
    author='zabbix-byte',
    license='MIT',
    test_suite="tests",
    install_reqs = ['cefpython3==66.1', 'Jinja2==3.1.2'],
    entry_points={
        'console_scripts': [
            'pypulse-manage = pypulse.manage:main'
        ]
    },
)