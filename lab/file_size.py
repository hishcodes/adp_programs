import os

dir_path = 'D:\\AAA\\BBB\\CCC\\DDD\\'
os.chdir(dir_path)

total_size = 0

all_files = os.listdir()

for file in all_files:
    each_size = os.path.getsize(str(dir_path) + str(file))
    total_size += each_size

print(total_size)