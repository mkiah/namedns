from setuptools import setup

setup(
    name='namedns',
    version='0.1',
    author='Mitch Kiah',
    author_email='mitch@mitchkiah.com',
    description=("Tool to manage domains and DNS records using"
                 "Name.com API."),
    keywords="namedotcom name.com namedns donutsinc",
    # url="https://gitlab.com/mitchkiah/namedns",
    py_modules['cli'],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        namedns=cli:cli
    ''',
)