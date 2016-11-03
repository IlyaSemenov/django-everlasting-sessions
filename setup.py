"""Django middleware that prevents user sessions from expiration."""
from setuptools import setup, find_packages


setup(
	name='django-everlasting-sessions',
	version='0.0.4',
	url='https://github.com/IlyaSemenov/django-everlasting-sessions',
	license='BSD',
	author='Ilya Semenov',
	author_email='ilya@semenov.co',
	description=__doc__,
	long_description=open('README.rst').read(),
	packages=find_packages(),
        include_package_data=True,
	zip_safe=False,
	platforms='any',
	install_requires=[],
	classifiers=[],
)
