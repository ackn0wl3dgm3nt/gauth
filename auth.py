from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

if not os.path.exists('credentials.json'):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    exit()
