import threading 
import shutil
import time
import os

#Give the path of destination folder you are going to copy to.
dest_path="M:\music"

def copy(file):
#I used this below line of code to join the path for the files in subdir.    
    for root,subdirs,files in os.walk(file):
        print("root",root)
#if part checks for files and copies files  
    if os.path.isfile(file):
        shutil.copy(file,dest_path)
#checks for dir/subdirs and copies them with the orginal file name in the source folder
    elif os.path.isdir(file):
        folder=os.path.join(root,file)
        name=file.split('\\')[-1]
        temp_dest=os.path.join(dest_path,name)
    
        shutil.copytree(folder,temp_dest)
#list of files you want to copy to the destination folder
files=["M:\\New folder (2)\\sql1.mp4","M:\\New folder (2)\\vp.mp4"]
#spliting list to do threading
file1=files[:1]
file2=files[1:2]
def copy1(splited_files):
    for file in splited_files:
        copy(file)
        
t=time.time()
t1=threading.Thread(target=copy1,args=(file1,))
t2=threading.Thread(target=copy1,args=(file2,))
t1.start()
t2.start()
t1.join()
t2.join()


print('done in:',time.time()-t)
