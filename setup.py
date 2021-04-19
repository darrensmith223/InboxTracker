from setuptools import setup, find_packages


setup(
    name='inboxtracker',
    version='1.0.0',
    author='Darren Smith',
    author_email='darren.smith@sparkpost.com',
    packages=find_packages(),
    url='https://github.com/darrensmith223/InboxTracker',
    license='Apache 2.0',
    description='Inbox Tracker Python API Library',
    install_requires=['requests>=2.20.1']
)