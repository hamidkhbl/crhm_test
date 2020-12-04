import filecmp
import os
from os import listdir

# set your obs files directory here
files_dir = 'ubuntu_output/'

# Get obs files in the directory
files = []
for file in os.listdir(files_dir):
    if file.endswith(".obs"):
        files.append(file)

file_count = len(files)
same_files = []
all_same_files = []

# Compare files and make categories
i = 0
print('Number of files: ',file_count)
while i < file_count:
    j = 0
    same_files.append(files[i])
    while j < file_count:
        if i != j:
            same = filecmp.cmp(files_dir + files[i], files_dir + files[j])
            if same:
                same_files.append(files[j])
        j+=1
    all_same_files.append(sorted(same_files))
    same_files = []
    i+=1

all_same_files = set(tuple(x) for x in all_same_files)

print('There are ', len(all_same_files),' Categories: ')
for i in all_same_files:
    print(i, 'Length: ', len(i))