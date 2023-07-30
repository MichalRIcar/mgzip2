"""This module provide a simple replacement of Python internal gzip module
to provide a multiprocessing solution for gzip compression/decompression.

License: MIT LICENSE
Copyright (c) 2019 Vincent Li | 2023 updates Michal Ricar

"""

from .multiProcGzip import MultiGzipFile, open, compress, decompress, __version__

__all__ = ["GzipFile", "open", "compress", "decompress"]

GzipFile = MultiGzipFile
