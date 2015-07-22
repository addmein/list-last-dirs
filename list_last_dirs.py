import os, pickle

dir = "B:\DTP DEPARTMENT\LIBRARY TIF"

def get_subs(dir):
    return [name for name in os.listdir(dir)
        if os.path.isdir(os.path.join(dir, name))]

def list_subdirs():
    list_subdirs =[]
    level1 = get_subs(dir)
    for subdir in level1:
        path = os.path.join(dir, subdir)
        list_subdirs.append(path)
    return list_subdirs

def check_for_eps(dir):
    epsdirlist = []
    for dirpath, dirnames, files in os.walk(dir):
        if files:
            print dirpath
            epsdirlist.append(dirpath)
    return epsdirlist
        
def createfolderlist(list):
    with open("tiffolderlist.txt", 'wb') as f:
        pickle.dump(list, f)
    
createfolderlist(check_for_eps(dir))
    
print "=" * 150
print "TASK COMPLETED"