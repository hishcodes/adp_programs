import os

for current_folder, sub_folders, filenames in os.walk('D:\\AAA'):
    print('\n\nCurrent folder is ' + current_folder)

    for sub_folder in sub_folders:
        print('\nThe subfolder of '+current_folder+' is '+sub_folder)

    for file in filenames:
        print('Folder '+sub_folder+' has the file '+file)