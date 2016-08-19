try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Una app para dominar el mundo',
    'author': 'Hugo Garcia',
    'url': 'https://github.com/hugoallan9/codigosClase.git',
    'download_url': 'https://github.com/hugoallan9/codigosClase.git/skeleton',
    'author_email': 'hugoallangm@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['App'],
    'scripts': [],
    'name': 'Mi preyecto'
    }

setup(**config)
