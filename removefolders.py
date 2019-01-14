import os

for i in range(1, 10):
    if os.path.exists("dir_{}".format(i)):
        os.rmdir("dir_{}".format(i))