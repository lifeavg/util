from setuptools import setup, find_packages

setup(
        name ='fake_zip_code',
        version ='0.1.0',
        author ='lifeavg',
        url ='https://github.com/lifeavg/util/fake_zip_code',
        description ='Zip code generator.',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'eszip = fake_zip_code.spain:main'
            ]
        },
        classifiers = ["Programming Language :: Python :: 3",
                       "Operating System :: OS Independent"],
        zip_safe = False
)
