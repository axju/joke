import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

def readme():
    with open('README.rst') as f:
        return f.read()

about = {}
with open(os.path.join(base_dir, 'joke', '__about__.py')) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],

    packages=find_packages(exclude=['examples', 'tests']),
    long_description=readme(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'requests',
        'html2text',
    ],

    entry_points = {
        'console_scripts': [
            'joke=joke.__main__:main',
        ],
    },

    keywords='joke fun funny',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Games/Entertainment',
        'Topic :: Internet',
        'Environment :: Console',
    ],
)
