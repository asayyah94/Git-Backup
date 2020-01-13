from filecmp import dircmp
from os import path
from os import popen
from os import makedirs
from os import remove
from shutil import copytree

backup="/Users/amirhossein/Documents/backup"

source="/Users/amirhossein/Documents/GitHub"

restart_backup = False

backup_number = 0

if os.path.exists(backup):
	get_all_changed(source, path.join(backup,source))

    if restart_backup:
		popen("cd " + path.join(backup,source) + "; " + "git checkout --orphan latest_branch; " + "git add -A; " + "git commit -m backup 1; " + "git branch -D master; " + "git branch -m master;")
	popen("cd " + path.join(backup,source) + "; " + "git add -A; " + "git commit -m backup 2; ")
    
else:
	makedirs(path.join(backup,source))
    copytree(source,path.join(backup,source))
    popen("cd " + path.join(backup,source) + "; " + "git init; git add -A; " + "git commit -m backup 1; ")


def set_all_changed(dir1, dir2):
    compared = dircmp(dir1, dir2)
    for subdir in compared.left_only:
        copytree(path.join(dir1, subdir),path.join(dir2, subdir))
        print("new: source: ", path.join(dir1, subdir), " dest: ", path.join(dir2, subdir))
    for subdir in compared.right_only:
        remove(path.join(dir2,subdir))
        print("deleted: ", path.join(dir2,subdir))
    for subdir in compared.diff_files:
        copytree(path.join(dir1, subdir),path.join(dir2, subdir))
        print("modified: source: ", path.join(dir1, subdir), " dest: ", path.join(dir2, subdir))
    for subdir in compared.funny_files:
        pass
    for subdir in compared.common_dirs:
        get_all_changed(path.join(dir1, subdir), path.join(dir2, subdir))

