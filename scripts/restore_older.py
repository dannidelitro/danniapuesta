import glob
import os
gits = glob.glob(r'C:\Users\dany\AppData\Local\GitHubDesktop\app-*\resources\app\git\cmd\git.exe')
if gits:
    os.system(f'"{gits[0]}" checkout 34fea8e8b767607e21929b0e2241da8124cd368a -- blog/')
    print("restored from older commit")
