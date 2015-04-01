# coding=utf-8
from distutils.core import setup
from setuptools import setup, find_packages

"""
Django middleware that prevents user sessions from expiration.
"""

setup(
	name='django-everlasting-sessions',
	version='0.0.4',
	url='https://github.com/IlyaSemenov/django-everlasting-sessions',
	license='BSD',
	author='Ilya Semenov',
	author_email='ilya@semenov.co',
	description='Django middleware that prevents user sessions from expiration.',
	long_description=__doc__,
	packages=find_packages(),
        include_package_data=True,
	zip_safe=False,
	platforms='any',
	install_requires=[],
	classifiers=[],
)
