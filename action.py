#!/usr/bin/python

import sys
import os

def print_help():
    print "need some help ?"

def getDestination():
    return "/tank/ecole/classer/"

destination = getDestination()
logPath = "torrentProcessor.log"
logFile = file(logPath, 'w')
sys.stdout = logFile

if sys.argv.count < 2:
    print_help()
    exit(1)

torrent_name = sys.argv[0]
torrent_path = sys.argv[1]

if os.path.isfile(torrent_path):
    #torrent is a single file
    print "Copying torrent " + torrent_name +  " from file " + torrent_path + " to destination " + getDestination() +torrent_name
    copyfile(torrent_path, getDestination()+torrent_name)
else:
    #torrent is a directory torrent_path + torrent_name
    print "moving directory not yet implemented"
