import os
from shutil import copyfile

srcMainPath = "/mnt/c/Users/dominik/Desktop/tel/Camera"
destMainPath = "/mnt/c/Users/dominik/Desktop/tel/Events"
listDirectoryNames = []

for fileName in os.listdir(srcMainPath):
	newDirectoryName = fileName[0:4] + "_" + fileName[4:6] + "_" + fileName[6:8] + "_"
	if not newDirectoryName in listDirectoryNames:
		listDirectoryNames.append(newDirectoryName)
		os.mkdir(destMainPath + "/" + newDirectoryName)
	src = srcMainPath + "/" + fileName
	dest = destMainPath + "/" + newDirectoryName + "/" + fileName
	copyfile(src, dest)
