# This script is meant to crawl through a user selected hard drive,
# and show them all their folders;
import os

# choose a drive
driveLetter = input('Enter drive letter: ')

driveName = driveLetter + ':/'

# Building a class to handle directories
# Might be a good idea to determine a root folder
class DirectoryManager:
    def __init__(self, dir, drive):
        self.drive = drive
        self.dir = dir

    # Function to get directory count of chosen drive
    def getDirectoryCount(self):
        if os.path.exists(self.drive):
            count = 0
            allDirectories = os.listdir(self.drive)
            for name in allDirectories:
                count = count+1
            fileAndFolder = ("File and Folder count: %d" % count)
            return fileAndFolder
        else:
            return "Drive doesn't exist or improper format"

    # Function to list all folders/directories within drive
    def listAllDirectories(self):
        if os.path.exists(self.drive):
            allDirectories = os.listdir(self.drive)
            return allDirectories
        else:
            return "Drive doesn't exist or improper format"





dDrive = DirectoryManager('', driveName)
print(dDrive.getDirectoryCount())
print(dDrive.listAllDirectories())