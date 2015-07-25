from setuptools import setup

setup(
    name='djangosprint',
    version='1.0',
    description='djangosprint.cf website',
    author='Grigory Petrov',
    author_email='grigory.v.p@gmail.com',
    url='http://djangosprint.cf/',
    install_requires=[
        'Django==1.8.1',
        'django-pipeline==1.5.2',
        'pillow==2.9.0'
    ],
)

