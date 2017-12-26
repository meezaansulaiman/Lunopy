__author__ = 'meezaan'

"""A Setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consitent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname((__file__)))

# Get the long description from the relevant file
#with open(path.join(here, "Description.rst"), encoding="utf-8") as f:
#    long_descrition = f.read()

setup(
    name="LunoPy",

    # Version should comply with PEP440.
    version="1.0.0",

    description="Python wrapper for Luno Api's",

    author="Meezaan Sulaiman",
    author_email="",
    packages=['lunopy'],
    install_requires=[
        'asyncio==3.4.3',
        'bleach==2.1.2',
        'certifi==2017.11.5',
        'chardet==3.0.4',
        'decorator==4.1.2',
        'entrypoints==0.2.3',
        'html5lib==1.0.1',
        'idna==2.6',
        'ipykernel==4.7.0',
        'ipython==6.2.1',
        'ipython-genutils==0.2.0',
        'ipywidgets==7.0.5',
        'jedi==0.11.0',
        'Jinja2==2.10',
        'jsonschema==2.6.0',
        'jupyter==1.0.0',
        'jupyter-client==5.1.0',
        'jupyter-console==5.2.0',
        'jupyter-core==4.4.0',
        'MarkupSafe==1.0',
        'mistune==0.8.3',
        'nbconvert==5.3.1',
        'nbformat==4.4.0',
        'notebook==5.2.2',
        'numpy==1.13.3',
        'pandas==0.21.0',
        'pandocfilters==1.4.2',
        'parso==0.1.0',
        'pexpect==4.3.0',
        'pickleshare==0.7.4',
        'prompt-toolkit==1.0.15',
        'ptyprocess==0.5.2',
        'Pygments==2.2.0',
        'python-dateutil==2.6.1',
        'pytz==2017.3',
        'pyzmq==16.0.3',
        'qtconsole==4.3.1',
        'requests==2.18.4',
        'simplegeneric==0.8.1',
        'six==1.11.0',
        'terminado==0.8.1',
        'testpath==0.3.1',
        'tornado==4.5.2',
        'traitlets==4.3.2',
        'urllib3==1.22',
        'wcwidth==0.1.7',
        'webencodings==0.5.1',
        'websockets==4.0.1',
        'widgetsnbextension==3.0.8'
    ],

    classifiers=[
        # How mature is this project?
        # 1 - Alpha
        # 2 - Beta
        # 3 - Production/Stable
        "Development Status :: 1 - Alpha",
        "Programming Language :: Python :: 3.5",
    ]
)
