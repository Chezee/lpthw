try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description' : 'MyProject',
    'author' : 'Chezee',
    'url' : 'https://github.com/Chezee',
    'download_url' : 'https://github.com/Chezee/lpthw',
    'author_email' : 'i.chezee@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : 'NAME',
    'scripts' : [],
    'name' : 'projectname',
    }
    
setup(**config)