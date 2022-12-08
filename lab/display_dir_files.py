import os

dir_path = input("Enter the directory path ")
os.chdir(dir_path)

all_files = os.listdir()

for file in all_files:
    print(file)

