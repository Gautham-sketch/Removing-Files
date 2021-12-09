import os
import shutil
import time

path = input("Enter your file location :- ")
day = input("Enter your days :- ")
time.time()

if os.path.exists(path) :
    os.walk(path)
    os.path.join()
    ctime = os.stat(path).st_ctime
    return ctime
else :
    print("File not found")