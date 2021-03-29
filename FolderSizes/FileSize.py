# This script is meant to crawl through a user selected hard drive,
# and show them all their folders;
import os

#choose a drive 
driveLetter = input('Enter drive letter: ')

drive = driveLetter + ':/'

#Function to get directory count of chosen drive
def getDirectoryCount(location):
    if os.path.exists(location):
        count = 0
        allDirectories = os.listdir(location)
        for name in allDirectories:
            count = count+1
        fileAndFolder = ("File and Folder count: %d" %count)
        return fileAndFolder
    else:
        return "Drive doesn't exist or improper format"

    
#Function to list all folders/directories within drive 
def listAllDirectories(location):
    if os.path.exists(location):
        allDirectories = os.listdir(location)
        return allDirectories
    else:
        return "Drive doesn't exist or improper format"


#Building a class to handle directories
#Class will use the above functions to find directories
#Might be a good idea to determine a root folder
class DirectoryManager:
    def __init__(dir, root):
        self.root = root
        self.dir = dir
        
    #Function to get directory count of chosen drive
    def getDirectoryCount():
    if os.path.exists(self.root):
        count = 0
        allDirectories = os.listdir(location)
        for name in allDirectories:
            count = count+1
        fileAndFolder = ("File and Folder count: %d" %count)
        return fileAndFolder
    else:
        return "Drive doesn't exist or improper format"


print(listAllDirectories(drive))
print(getDirectoryCount(drive))