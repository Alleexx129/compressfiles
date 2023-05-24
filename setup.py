from setuptools import setup, find_packages

setup(
    name='txt-compressor',
    VERSION='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'gzip',
        'typing',
        'tqdm'
    ],
    LONG_DESCRIPTION='A small library to compress txt files using gzip',
    DESCRIPTION='compress txt files',
    keywords=['python', 'txt', 'compress', 'txt-compressor']
     url='https://github.com/Alleexx129/txt-compressor/new/main',
    license='MIT',
)
