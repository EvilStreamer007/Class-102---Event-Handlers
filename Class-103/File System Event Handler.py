from fileinput import filename
import sys
import time
import random

import os 
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

toDir = '/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-103/tempDownloads/'
fromDir = '/Users/chaitalishah/Downloads/'

dirTree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class fileMovement(FileSystemEventHandler):
    def on_created(self,event):
        print(event)
        print(event.src_path)
        name, extension = os.path.splitext(event.src_path)
        for key, value in dirTree.items():
            if extension in value:
                fileName = os.path.basename(event.src_path)
                path1 = fromDir + '/' + fileName
                path2 = toDir + '/' + key
                path3 = toDir + '/' + key + '/' + fileName

                if os.path.exists(toDir + "/" + key):
                    if os.path.exists(path2):
                        print("Moving..." + fileName)
                        shutil.move(path1, path3)
                    else:
                        os.mkdir(path2)
                        print("Moving..." + fileName)
                        shutil.move(path1, path3)

eventHandler = fileMovement()
Observer1 = Observer()
Observer1.schedule(eventHandler,fromDir,recursive = True)
Observer1.start()

try:
    while True:
        time.sleep(3)
        print("Working..")
except KeyboardInterrupt:
    Observer1.stop()
    print("\Program Ended.")