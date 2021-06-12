# 1. List all files inside specified foler
# 2. Create new folders for text, audio, video and image
# 3. Move files into newly created folder based on extention

import os
import shutil

path = "/Users/Thato/Desktop/2021/Programming/Python/SimplePythonProjects/Master/foldersorter/document/"
#listdir() will list all files and save into a list
names = os.listdir(path)
print(names)
folder_name = ['image', 'music', 'gif', 'video', 'pdf', 'word documents', 'powerpoint presentations', 'excel spreadsheets', 'applications', 'zipfiles']  
#Create range from number of folder types + 1
# 0 = image, 1 = music 2= do nothing
for x in range(0,10):
    #check if folder exists, then add a folder to the given path
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x]) #makedirs creates new folder and takes the directory as a parameter
for files in names:
    if ".jpeg" in files and not os.path.exists(path+'image/'+files): #Check if files already don't exist in directory
        shutil.move(path+files, path+'image/'+files)

    if ".mp3" in files and not os.path.exists(path+'music/'+files):
        shutil.move(path+files, path+'music/'+files)

    if ".flac" in files and not os.path.exists(path+'music/'+files):
        shutil.move(path+files, path+'music/'+files)

    if ".wav" in files and not os.path.exists(path+'music/'+files):
        shutil.move(path+files, path+'music/'+files)

    if ".jpg" in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files, path+'image/'+files)

    if ".png" in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files, path+'image/'+files)

    if ".gif" in files and not os.path.exists(path+'gif/'+files):
        shutil.move(path+files, path+'gif/'+files)
    
    if ".mp4" in files and not os.path.exists(path+'video/'+files):
        shutil.move(path+files, path+'video/'+files)
     
    if ".MOV" in files and not os.path.exists(path+'video/'+files):
        shutil.move(path+files, path+'video/'+files)
     
    if ".AVI" in files and not os.path.exists(path+'video/'+files):
        shutil.move(path+files, path+'video/'+files)

    if ".docx" in files and not os.path.exists(path+'word documents/'+files):
        shutil.move(path+files, path+'word documents/'+files)

    if ".pdf" in files and not os.path.exists(path+'pdf/'+files):
        shutil.move(path+files, path+'pdf/'+files)

    if ".ppt" in files and not os.path.exists(path+'powerpoint presentations/'+files):
        shutil.move(path+files, path+'powerpoint presentations/'+files)

    if ".pptx" in files and not os.path.exists(path+'powerpoint presentations/'+files):
        shutil.move(path+files, path+'powerpoint presentations/'+files)

    if ".xlsx" in files and not os.path.exists(path+'excel spreadsheets/'+files):
        shutil.move(path+files, path+'excel spreadsheets/'+files)

    if ".exe" in files and not os.path.exists(path+'applications/'+files):
        shutil.move(path+files, path+'applications/'+files)

    if ".zip" in files and not os.path.exists(path+'zipfiles/'+files):
        shutil.move(path+files, path+'zipfiles/'+files)

    