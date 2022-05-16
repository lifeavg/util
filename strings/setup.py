from setuptools import setup, find_packages

setup(
        name ='strings',
        version ='0.1.0',
        author ='lifeavg',
        url ='https://github.com/lifeavg/util/strings',
        description ='CLI string tools.',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'str = strings.strings:main'
            ]
        },
        classifiers = ["Programming Language :: Python :: 3",
                       "Operating System :: OS Independent"],
        zip_safe = False
)
