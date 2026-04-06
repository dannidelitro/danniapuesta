import glob
import os
gits = glob.glob(r'C:\Users\dany\AppData\Local\GitHubDesktop\app-*\resources\app\git\cmd\git.exe')
if gits:
    os.system(f'"{gits[0]}" checkout e5a1860ceb957bf62fdd19830c06cb81694d886e -- blog/')
    print("restored from commit")
