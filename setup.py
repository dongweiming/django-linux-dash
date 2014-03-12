import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requires = ['psutil', 'django']

if sys.platform == 'darwin':
    requires.append('netifaces')

setup(
    name='django-linux-dash',
    version='0.1',
    description='A clone of linux-dash written in Django, Also Support OS X, Most use psutils, Not use systemcall method.',
    long_description=README,
    author='Dongweiming',
    author_email='ciici123@gmail.com',
    url='https://github.com/dongweiming/django-linux-dash/',
    download_url = '',
    packages=['dash'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    license="MIT",
    classifiers = '',
    zip_safe=False,
)
