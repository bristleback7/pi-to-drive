import os
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
folder = '1lxctf3LzEL2037_X0ZhvKqlsCebCi7IG'
upload_folder = sys.argv[1]
upload_file_list = os.listdir(upload_folder)

if len(upload_file_list) > 0:
  question = input(f"""
Uploading files:
{upload_file_list[0]}
..
{upload_file_list[-1]}.
Press [ENTER] to continue or Ctrl-c to cancel upload: """)

for upload_file in upload_file_list:
    print(f'Uploading file {upload_file}')
    file1 = drive.CreateFile({'parents': [{'id': folder}], 'title': upload_file})
    upload_file_full_path = os.path.join(upload_folder, upload_file)
    file1.SetContentFile(upload_file_full_path)
    file1.Upload()
