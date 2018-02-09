#!/usr/bin/python

import sys

path_strip = "http://www.the-associates.co.uk"

for line in sys.stdin:
	data = line.strip().split(" ")
	if (len(data) == 10):
		ip, ident, username, date, tz, method, path, query, status, size = data		
		if (path_strip in path):
			path = path.replace(path_strip, '')
		print path