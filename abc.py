import os 
import shutil

path = os.getcwd()
print(path)

name,ext = os.path.splitext('/Users/varshitha/Downloads/Pendulum.pdf')
print('the name of the file is: ', name)
print('the extention of the file is: ', ext) 


from_dir = '/Users/varshitha/Downloads'
to_dir = '/Users/varshitha/Downloads/Document_Files'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files : 
    name,ext = os.path.splitext(i)
    if ext == '':
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + i 
        path2 = to_dir + '/' + 'Document_Files"'
        path3 = to_dir + '/' + 'Document_Files' + '/' + i
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1,path3) #shifting first path to second
        else:
            os.makedirs(path2)
            print('creating and moving')
            shutil.move(path,path3)
        