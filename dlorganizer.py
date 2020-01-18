#!/usr/bin/env python

#This is an program use to automaticly organize my files in the 'download folder'

import os
import shutil

#path of my download folder
path = "/Users/jonathanthai/Downloads/"
listpath = os.listdir(path)

#Init variable and list
audio_directory = 'audio'
compressed_directory = 'compressed'
disc_directory = 'disc'
data_directory = 'data'
executable_directory = 'executable'
img_directory = 'img'
font_directory = 'font'
doc_directory = 'doc'
programming_directory = 'programming'
video_directory = 'video'
other_directory = 'otherfiles'

directory = (audio_directory, compressed_directory, disc_directory, data_directory, executable_directory, img_directory, font_directory, doc_directory, programming_directory, video_directory, other_directory)

myaudio = (".aif", ".cda", ".mid", ".midi", ".mpa", ".ogg", ".wav", ".wpl", ".mp3", ".wma")
mycompressed = (".zip", ".tar", ".7z", ".arg", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z")
mydisc = (".dmg", ".iso", ".bin", ".toast", "vcd")
mydata = (".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".xml")
myexecutable = (".app", ".apk", ".exe", ".bat", ".cgi", ".pl", ".com", ".gadget", ".jar", ".wsf")
myimg = (".ai", ".jpg", ".png", ".gif", ".jpeg", ".svg", ".bmp", ".ico", ".ps", ".psd", ".tif", ".tiff")
myfont = (".fnt", ".fon", ".otf", ".ttf")
mydoc = (".doc", ".docx", ".key", ".odp", ".odt", ".pps", ".ppt", ".pttx", ".ods", ".txt", ".pdf", ".xlr", ".xls", ".xlsx", "rtf", ".tex", ".wks", ".wps", ".wpd")
myprogram = (".c", ".class", ".cpp", ".cs", ".h", ".java", ".sh", ".switft", ".vb", ".py", ".htm", ".html")
myvideo = (".mov", ".mp4", ".wmv", ".avi", ".m4a", ".m4v", ".mpg", ".mpeg", ".3g2", ".3gp", ".flv", ".h264", ".mkv", ".rm", ".swf", ".vob")

def main():
    print(listpath)

#Creating folders

    for folder in directory:
        if not folder in listpath:
            os.mkdir(path+folder)

#Orgazing files into folders

    for file in listpath:
        if file.endswith(myaudio):
            shutil.move(os.path.join(path,file), os.path.join(path+audio_directory,file))
        elif file.endswith(mycompressed):
            shutil.move(os.path.join(path,file), os.path.join(path+compressed_directory,file))
        elif file.endswith(mydisc):
            shutil.move(os.path.join(path,file), os.path.join(path+disc_directory,file))
        elif file.endswith(mydata):
            shutil.move(os.path.join(path,file), os.path.join(path+data_directory,file))
        elif file.endswith(myexecutable):
            shutil.move(os.path.join(path,file), os.path.join(path+executable_directory,file))
        elif file.endswith(myimg):
            shutil.move(os.path.join(path,file), os.path.join(path+img_directory))
        elif file.endswith(myfont):
            shutil.move(os.path.join(path,file), os.path.join(path+font_directory))
        elif file.endswith(mydoc):
            shutil.move(os.path.join(path,file), os.path.join(path+doc_directory))
        elif file.endswith(myprogram):
            shutil.move(os.path.join(path,file), os.path.join(path+programming_directory))
        elif file.endswith(myvideo):
            shutil.move(os.path.join(path,file), os.path.join(path+video_directory))
        else:
            shutil.move(os.path.join(path,file), os.path.join(path+other_directory))

if __name__ == "__main__":
    main()
