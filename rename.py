import os

def rename_files(directory):
    files = os.listdir(directory)
    for file in files:
        new_name = file.lstrip('0')
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

subdirectories = ['c2', 'c3', 'c4', 'c5', 'c6', 'hg']

for subdirectory in subdirectories:
    rename_files(os.path.join('banco', subdirectory))