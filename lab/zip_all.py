import os, zipfile

os.chdir('D:\\AAA')

newZip = zipfile.ZipFile('new.zip', 'a')
for files in list(os.listdir('D:\\AAA')):
    newZip.write(files, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()