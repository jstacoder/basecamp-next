import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

required = ['requests>=1.0.0']

setup(
    name='bcnxt',
    version='0.2.0',
    author='Kyle Roux',
    author_email='kyle@level2designs.com',
    description=('Wrapper for Basecamp Next API.'),
    license="BSD",
    keywords="basecamp bcx api basecamp-next",
    url='https://github.com/jstacoder/basecamp-next',
    packages=['bcnxt'],
    install_requires=required,
    long_description=read('README.rst'),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
    ],
)
