# GZip Compression Utility

This is a Python package that provides a simple utility for compressing and decompressing files using the GZip format. The package uses the `gzip` module from the Python standard library.

## Installation

You can install the package using pip:

pip install txt-compressor



## Usage

The package provides two main functions: `compress()` and `decompress()`. 

### Compressing a txt file

To compress a file, use the `compress()` function. For example:

from txt-compressor import compress

compress('my_file.txt')



This will compress `my_file.txt` and save the compressed file as `my_file.gz`.

You can also specify the output file path using the `output_file_path` parameter:

compress('my_file.txt','my_file.gz')
You can customize the compression level (0-9), default is '6'
compress('C:/Users/the_name/downloads/my_file.txt','my_file', '8') # don't put .gz for the output or it will be my_file.gz.gz
It is supposed to output my_file.gz 
### Decompressing a file

To decompress a file, use the `decompress()` function. For example:

from txt-compressor import decompress

decompress('my_file.gz')



This will decompress `my_file.gz` and save the decompressed file as `my_file.txt`.

You can also specify the output file path using the `output_file_path` parameter:

decompress('my_file.gz', 'my_file.txt')



## License

This project is licensed under the terms of the MIT license. See the `LICENSE` file for details.
