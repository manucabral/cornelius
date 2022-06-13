from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='cornelius',
    version='0.0.3',
    license='GPLv3',
    description='Python mouse and keyboard input control in a simple way.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Manuel Cabral',
    author_email='cabral.manuel@yandex.com',
    url='https://github.com/manucabral/cornelius',
    keywords=['mouseinput', 'keyboardinput', 'input', 'win32', 'inputcontrol'],
    packages=['cornelius'],
    python_requires='>= 3.2',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
)
