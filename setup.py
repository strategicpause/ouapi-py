from distutils.core import setup

setup(
    name='OUAPI',
    version='0.1.0',
    author='Nick Peters',
    author_email='npeters@omniupdate.com',
    packages=['ouapi'],
    scripts=[],
    url='http://www.omniupdate.com/',
    license='LICENSE.txt',
    description='Provides access to the OU Campus API.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)