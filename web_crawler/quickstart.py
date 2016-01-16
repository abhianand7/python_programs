import pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication

drive = GoogleDrive(gauth)
id = "1FTXLaN84KB6ra3JSTvycQb7dU9ekXUDToIg9x4MJsu0"

file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for file in file_list:
    print 'title : %s, id: %s' % (file['title'],file['id'])

'''new_file = drive.CreateFile({'id': id})

new_file.GetContentFile('response.xlsx','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
'''