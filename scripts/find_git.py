import glob
import os
import sys

gits = glob.glob(r'C:\Users\dany\AppData\Local\GitHubDesktop\app-*\resources\app\git\cmd\git.exe')
if gits:
    git_exec = gits[0]
    os.system(f'"{git_exec}" log --oneline -- blog/win-rate-roi-apuestas/index.html')
