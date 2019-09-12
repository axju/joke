from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        packages=find_packages(exclude=['examples', 'tests']),
        include_package_data=True,
        zip_safe=False,
        use_scm_version=True,

        setup_requires=[
            'setuptools_scm',
        ],
        install_requires=[
            'requests',
        ],

        entry_points={
            'console_scripts': [
                'joke=joke.__main__:main',
            ],
        },
    )
