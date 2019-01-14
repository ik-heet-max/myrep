import os

for i in range(1, 10):
    if not os.path.exists("dir_{}".format(i)):
        os.mkdir("dir_{}".format(i))