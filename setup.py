from setuptools import setup

setup(
    name='abdutils',
    version='0.1',
    description='A Python utility module that enhances the ease and reliability of Python programming.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ABD',
    author_email='abdkhan@163.com',
    url='https://github.com/abdkhanstd/abdutils',
    py_modules=['abdutil'],  # Specify the main module (Python file) to be included
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'Pillow==9.1.0',
        'opencv-python==4.8.1.78',
        'matplotlib==3.7.3',
        'numpy==1.23.1',
    ],
)
