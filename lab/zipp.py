import zipfile
import os
zip = zipfile.ZipFile('aaz.zip', 'w')

dir = 'D:\\aaa'
for foldername, subfolder, filename in os.walk(os.path.abspath(dir)):
    zip.write(foldername)
    for file in filename:
        zip.write(os.path.join(foldername, file), compress_type=zipfile.ZIP_DEFLATED)

zip.close()
