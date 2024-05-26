import shutil
import os
file_path = r'C:\Games\ffs.433030.ixbrl'

if os.path.exists(file_path):
    try:
        os.remove(file_path)
        print(f'{file_path} has been removed.')
    except Exception as e:
        print(f'An error occurred while removing {file_path}: {e}')
else:
    print(f'{file_path} does not exist.')

from pathlib import Path

directory_path = Path(r'C:\Games')

# List all files in the directory
files = [file for file in directory_path.iterdir() if file.is_file()]

# Print the list of files
for file in files:
    print(file)
