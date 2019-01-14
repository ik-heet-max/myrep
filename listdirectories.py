import os

dirPath = input("Enter path: ")
dirs = [i for i in os.listdir(dirPath) if os.path.isdir(os.path.join(dirPath, i))]
print(dirs)