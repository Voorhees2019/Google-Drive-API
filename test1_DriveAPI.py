from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

with open('test1.txt', 'r+') as file:
    file.write('something here')
    file_drive = drive.CreateFile({'title': os.path.basename(file.name)})
    file_drive.SetContentString(file.read())
    file_drive.Upload()
print(f'The file: {file} has been uploaded')
