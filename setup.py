from setuptools import setup, find_packages

setup(
   name='Films',
   version='0.0.1',
   author='Yann Plougonven',
   author_email='plougonven-y@saint-louis29.net',
   license='LICENSE.txt',
   description='Not an awesome program',
   long_description=open('README.md').read(),
   install_requires=[
       "",
   ],

    packages=find_packages(
        where='src',
    ),
    package_dir={"": "src"}

)
