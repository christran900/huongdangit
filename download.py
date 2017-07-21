import urllib2
import sys
url = raw_input("")
file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
files_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Byte: %s" %(file_name, files_size) 

files_size_dl = 0
block_sz = 8192
while True:
	buffer = u.read(block_sz)
	if not buffer:
		break
	files_size_dl += len(buffer)
	f.write(buffer)
	status =  r"%10d  [%3.2f%%]" % (files_size_dl, files_size_dl *100. / files_size)
	status = status + chr(8)*(len(status)+1)
	print status,
f.close()