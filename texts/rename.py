from datetime import datetime
import os
import glob
import shutil
import time


for filename in os.listdir():
    if filename[-3:] == ".py":
        continue
    n_filename = filename[:5]+".html"
    shutil.move(filename,n_filename)
