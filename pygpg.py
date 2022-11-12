import os

def check_file(file_path):
    os.chdir(file_path)
    print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(check_file(file_path+'/'+f))
            os.chdir(file_path)
        else:
            files.append(f)
            print(f)
    #return files

file_list = check_file(".")