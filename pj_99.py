import os
import shutil
path = 'E:/imtiyaz class folder'
print(" before coppying file:")
print(os.listdir(path))
source = "E:/imtiyaz class folder/backupfile.txt"
destination = "E:/imtiyaz class folder/backupfilecopy.txt"
dest = shutil.copy(source,destination)
print(" After copying file:")

print(os.listdir(path))