from setuptools import setup, find_packages

setup(
    name='txt-compressor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'gzip',
        'typing',
        'tqdm'
    ],
    author='Alleexx',
    author_email='Alleexx129@gmail.com',
    description='A txt file compressor',
    url='https://github.com/Alleexx129/txt-compressor/new/main',
    license='MIT',
)
