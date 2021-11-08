import os
import os.path
import shutil

os.chdir('main')
for cur_dir, dirs, files in os.walk('.'):
    for file in files:
        if file[-3:] == '.py':
            print(cur_dir[2:])
            break

print(dirs)