import gzip
import os
from pathlib import Path
from typing import Optional
from tqdm import tqdm


MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB, it can go higher
DEFAULT_CHUNK_SIZE = 1024 * 1024  # 1 MB
DEFAULT_COMPRESSION_LEVEL = 6  # The gzip compression level (0-9)

def compress(file_path: str, output_file_path: Optional[str] = None, compression_level: Optional[str] = None, chunk_size: int = DEFAULT_CHUNK_SIZE) -> str:
    """
    Compresses a file using gzip.

    Args:
        file_path (str): The path of the input file.
        output_file_path (str): The path of the output file. If not specified, a default name will be generated.
        chunk_size (int): The size of the chunks to read and write (in bytes). Defaults to 1 MB.
        compression_level (int): The gzip compression level (0-9). Defaults to 6.

    Returns:
        The path of the compressed file.
    """
    if compression_level == None or compression_level > 9:
      compression_level = DEFAULT_COMPRESSION_LEVEL
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE:
        print(f"Warning: {file_path} is a large file and may take a while to compress.")
    if output_file_path is None:
        # Generate default output file path based on input file path
        output_file_path = f"{os.path.splitext(file_path)[0]}.gz"
    else:
        # If output_file_path is specified by the user, append .gz extension
        output_file_path = f"{output_file_path}_compressed.gz"
    with open(file_path, 'rb') as input_file:
        with gzip.GzipFile(output_file_path, 'wb', compresslevel=compression_level) as output_file:
            with tqdm(total=file_size, unit='B', unit_scale=True,
                      desc=f'Compressing {os.path.basename(file_path)}') as pbar:
                while True:
                    chunk = input_file.read(chunk_size)
                    if not chunk:
                        break
                    output_file.write(chunk)
                    pbar.update(len(chunk))
    return output_file_path




def decompress(file_path: str, output_file_path: Optional[str] = None, chunk_size: int = DEFAULT_CHUNK_SIZE) -> str:
    """
    Decompresses a gzip file.

    Args:
        file_path (str): The path of the input file.
        output_file_path (str): The path of the output file. If not specified, a default name will be generated.
        chunk_size (int): The size of the chunks to read and write (in bytes). Defaults to 1 MB.

    Returns:
        The path of the decompressed file.
    """
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE:
        print(f"Warning: {file_path} is a large file and may take a while to decompress.")
    if output_file_path is None:
        output_file_path = os.path.splitext(file_path)[0]
    else:
        output_file_path = f"{output_file_path}.txt"
    with gzip.GzipFile(file_path, 'rb') as input_file:
        with open(output_file_path, 'wb') as output_file:
            with tqdm(total=file_size, unit='B', unit_scale=True,
                      desc=f'Decompressing {os.path.basename(file_path)}') as pbar:
                while True:
                    chunk = input_file.read(chunk_size)
                    if not chunk:
                        break
                    output_file.write(chunk)
                    pbar.update(len(chunk))
    return output_file_path


def read_file(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == '.gz':
        with gzip.open(file_path, 'rt') as f:
            return f.read()
    else:
        with open(file_path, 'r') as f:
            return f.read()
