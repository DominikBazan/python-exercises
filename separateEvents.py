import os
import sys
from shutil import copyfile

srcDir = sys.argv[1]
destDir = sys.argv[2]
listDirectoryNames = []

for fileName in os.listdir(srcDir):
	newDirectoryName = fileName[0:4] + "_"
	newDirectoryName += fileName[4:6] + "_"
	newDirectoryName += fileName[6:8] + "_"
	if not newDirectoryName in listDirectoryNames:
		listDirectoryNames.append(newDirectoryName)
		os.mkdir(destDir + "/" + newDirectoryName)
	src = srcDir + "/" + fileName
	dest = destDir + "/" + newDirectoryName + "/" + fileName
	copyfile(src, dest)
