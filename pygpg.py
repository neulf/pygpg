import os

USER_ID = ""

def check_file(file_path, reverse=False):
    if(file_path.startswith(".") and reverse == True):
        return
        
    if(reverse==False):
        file_path = os.path.abspath(file_path)
        
    #print("chdir："+os.path.abspath(file_path))
    os.chdir(file_path)
    
    #print(file_path)
    #print("当前目录："+os.path.abspath(file_path))
    all_file = os.listdir()
    files = []
    
    if all_file:
        for f in all_file:
            if not os.path.isdir(f):
                if(f.find(".") != 0 and f.endswith(".gpg")):
                    files.append(f)
    
        for f in all_file:
            if os.path.isdir(f):
                
                if(f.startswith(".")):
                    continue
                                                 
                #print(type(f))
                check_file(file_path+'/'+f,True)
                
                #os.chdir(os.path.abspath(file_path))
                os.chdir(file_path)
            else:
                if(f.startswith(".") or f.endswith(".gpg")):
                    continue
                
                if(f+".gpg" in files):
                    continue
                
                #print(files)
                print("-->开始加密："+f)
                print("gpg --batch --yes -r " + USER_ID + " -e " + f)
                
                
    #return files

file_list = check_file(r"./testgpg")