import os
import shutil

source="C:/Users/shiva/OneDrive/Pictures/Downloads"
move="C:/Users/shivaOneDrive/Pictures/Downloads"

list_of_files=os.listdir(source)
print(list_of_files)

for file in list_of_files:
    name,extention = os.path.splitext(file)
    print(name)
    print(extention)

    if extention=='':
        continue
    if extention in [ '.png', '.jpg', '.gif', '.jfif']:
        path1=source+'/'+file
        path2=move+'/'+'downloadsimages'
        path3=move+'/'+'downloadsimages'+'/'+file

        if os.path.exists(path2):
            print('Moving'+file+'.....')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Moving'+file+'.....')
            shutil.move(path1,path3)

