import os
import shutil

sourcepath="/Users/jonathanburnett/Downloads"
sourcefiles = os.listdir(sourcepath)
destinationpath = "/Users/jonathanburnett/Library/Application Support/Sports Interactive/Football Manager 2022/tactics"
for file in sourcefiles:
    if file.endswith('.fmf'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))