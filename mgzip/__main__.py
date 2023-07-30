"""This module provide a simple replacement of Python internal gzip module
to provide a multiprocessing solution for gzip compression/decompression.

License: MIT LICENSE
Copyright (c) 2019 Vincent Li | 2023 updates Michal Ricar

"""

import mgzip

def main(argv):
	decompress = False
	if argv and argv[0]=='-d':
		decompress = True
		argv=argv[1:]
	if decompress:
		f=mgzip.GzipFile(filename="", mode="rb", fileobj=sys.stdin.buffer, thread=4, blocksize=10**6)
		g=sys.stdout.buffer
	else:
		f=sys.stdin.buffer
		g=mgzip.GzipFile(filename="", mode="wb", fileobj=sys.stdout.buffer, thread=4, blocksize=10**6)
	while True:
		chunk = f.read(1024)
		if not chunk:
			break
		g.write(chunk)
	if g is not sys.stdout:
		g.close()
	if f is not sys.stdin:
		f.close()

if __name__=='__main__':
	import sys
	main(sys.argv[1:])
