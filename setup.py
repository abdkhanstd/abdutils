from setuptools import setup, find_packages

setup(
    name='abdutils',
    version='0.1',
    description='A Python utility module that enhances the ease and reliability of Python programming.',
    author='ABD',
    author_email='abdkhan@163.com',
    url='https://github.com/abdkhanstd/abdutils',
    packages=find_packages(),  # Automatically find all packages in the directory
    py_modules=['abdutils.abdutils'],  # Specify the main module (Python file) to be included
)
