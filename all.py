import os
import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import time
member=["zkx","lrm","wzy","oys","ygh","gch"]
for i in range(6):
    if os.path.exists(member[i]+"house.py"):
        os.system("D:/Python/python.exe "+member[i]+"house.py")