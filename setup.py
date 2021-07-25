# still working to understand how to write  .rst file
# so that all can download all packages by setup.py
from setuptools import setup

setup(
    name='opencv-codes-practice',
    version='0.4',
    description='run "python setup.py" to get all required libraries to get download',
    long_description=open('requirements.rst')

)