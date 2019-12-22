from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='namedns',
    version='0.1',
    author='Mitch Kiah',
    author_email='mitch@mitchkiah.com',
    description=("Tool to manage domains and DNS records using"
                 "Name.com API."),
    long_description=long_description,
    license='',
    keywords="namedotcom name.com namedns donutsinc",
    # url="https://gitlab.com/mitchkiah/namedns",
    packages=['namedns'],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        namedns=namedns.cli:cli
    ''',
)
