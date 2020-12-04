
#import numpy as np
import filecmp

files = []
for i in range(100):
    files.append('sc'+str(i+1)+'.obs')

#files = ['sc29.obs', 'sc22.obs', 'sc48.obs', 'sc90.obs', 'sc47.obs', 'sc71.obs', 'sc65.obs', 'sc4.obs', 'sc17.obs', 'sc46.obs', 'sc78.obs', 'sc93.obs', 'sc44.obs', 'sc72.obs', 'sc74.obs', 'sc69.obs', 'sc92.obs', 'sc64.obs', 'sc30.obs', 'sc49.obs', 'sc61.obs', 'sc70.obs', 'sc1.obs', 'sc37.obs', 'sc12.obs', 'sc9.obs', 'sc62.obs', 'sc97.obs', 'sc96.obs', 'sc40.obs', 'sc67.obs', 'sc7.obs', 'sc66.obs', 'sc56.obs', 'sc38.obs', 'sc31.obs', 'sc43.obs', 'sc76.obs']
file_count = len(files)
same_files = []

files_dir = '/Users/hamid/Code/crhm/3/crhmcode/release1.1/'

i = 0
print(file_count)
while i < file_count:
    j = 0
    while j < file_count:
        if i != j:
            same = filecmp.cmp(files_dir + files[i], files_dir + files[j])
            if same:
                same_files.append(files[j])
                same_files.append(files[i])
        j+=1
    i+=1
print(len(set(same_files)))
print(set(same_files))