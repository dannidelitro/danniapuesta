import glob
import os
gits = glob.glob(r'C:\Users\dany\AppData\Local\GitHubDesktop\app-*\resources\app\git\cmd\git.exe')
if gits:
    os.system(f'"{gits[0]}" log -n 5')
    os.system(f'"{gits[0]}" status')
