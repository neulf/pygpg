import os
import sys
import subprocess

USER_ID = ""
ROOT_PASS = ""

def check_file(file_path, reverse=False):
    if(file_path.startswith(".") and reverse == True):
        return
        
    if(reverse==False):
        file_path = os.path.abspath(file_path)
        if file_path.endswith("/"):
            file_path = file_path[:-1]
        
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
                if f.startswith("-"):
                    fname = "./" + f
                else:
                    fname = f
                
                cmd = 'sudo gpg --batch --yes -r ' + USER_ID + ' -e "' + fname + '"'
                print("-->开始加密：" + cmd)
                #r = subprocess.call(cmd,shell=True)
                
                (status, result)=subprocess.getstatusoutput('echo %s| sudo -S %s' %(ROOT_PASS,cmd))
                print("-->执行结果：" + str(result))
                
                
    #return files

if len(sys.argv) <= 1:
    print("Please input filepath.")
else:
    file_list = check_file(sys.argv[1])