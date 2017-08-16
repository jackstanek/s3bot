from setuptools import setup, find_packages

setup(
    name='s3bot',
    version='0.0.1',
    description='BotBot-adjacent resource manager',
    url="https://github.com/jackstanek/s3bot",
    author="Jack Stanek",
    license="MIT",
    author_email="stane064@umn.edu",
    package_dir={'':'src'},
    packages=['s3bot'],
    scripts=['bin/s3bot']
)
