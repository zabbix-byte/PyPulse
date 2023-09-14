from setuptools import find_packages, setup

setup(
    name='python-pulse',
    packages=find_packages(),
    version='0.1',
    description='Python, create desktop applications based on Chromium',
    author='zabbix-byte',
    license='MIT',
    install_requires=['cefpython3==66.1', 'Jinja2==3.1.2', 'wxPython==4.2.1'],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'pypulse-manage = pypulse.manage:main'
        ]
    },
)
