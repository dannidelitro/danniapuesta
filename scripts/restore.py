import glob
import os

gits = glob.glob(r'C:\Users\dany\AppData\Local\GitHubDesktop\app-*\resources\app\git\cmd\git.exe')
if gits:
    git_path = gits[0]
    print("Found git:", git_path)
    os.system(f'"{git_path}" checkout HEAD -- blog/')
    print("Restored.")
else:
    print("Git not found!")
