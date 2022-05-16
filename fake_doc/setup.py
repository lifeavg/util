from setuptools import setup, find_packages

setup(
        name ='fake_doc',
        version ='0.1.0',
        author ='lifeavg',
        url ='https://github.com/lifeavg/util/fake_doc',
        description ='Fake doc number generator.',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'esdoc = fake_doc.spain:main'
            ]
        },
        classifiers = ["Programming Language :: Python :: 3",
                       "Operating System :: OS Independent"],
        zip_safe = False
)
