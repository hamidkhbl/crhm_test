import filecmp
from os import listdir
from os.path import isfile, join

files_dir = 'mac_output/'

files = [f for f in listdir(files_dir) if isfile(join(files_dir, f))]

file_count = len(files)
same_files = []
all_same_files = []



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

print('There are ', len(all_same_files),' Categorie(s): ')
for i in all_same_files:
    print(i, 'Length: ', len(i))