import os

def check_file(file_path, reverse=False):
    if(file_path.find(".") == 0 and reverse == True):
        return
        
    #print("->"+file_path)
    os.chdir(file_path)
    #print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    
    if all_file:
        for f in all_file:
            if os.path.isdir(f):
                
                if(f.find(".") == 0):
                    continue
                                                 
                #print(type(f))
                check_file(file_path+'/'+f,True)
                os.chdir(file_path)
            else:
                if(f.find(".") == 0):
                    continue
                #files.append(f)
                print("--->"+f)
    #return files

file_list = check_file(".")