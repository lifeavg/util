from setuptools import setup, find_packages

REQUIREMENTS = ['python-magic-bin']

setup(
        name ='b64',
        version ='0.1.0',
        author ='lifeavg',
        url ='https://github.com/lifeavg/util/b64',
        description ='Base64encoder/decoder for files and strings.',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'b64 = b64.b64:main'
            ]
        },
        classifiers = ["Programming Language :: Python :: 3",
                       "Operating System :: Windows"],
        install_requires = REQUIREMENTS,
        zip_safe = False
)
