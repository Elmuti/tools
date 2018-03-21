# File downloader - downloads files from a list
# Usage:
# python downloader.py links.txt /downloaddir/
import urllib, sys
links = sys.argv[1]
dldir = sys.argv[2]

for line in open(links, "r"):
    filename = line.split("/")[-1].rstrip('\n')
    filepath = dldir+filename
    print "Downloading: ",filename
    urllib.urlretrieve(line, filepath)
