from setuptools import setup, find_packages

setup(
    name='my_package',
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
    description='A description of your package',
    url='https://github.com/Alleexx129/txt-compressor/new/main',
    license='MIT',
)
