import os
ret_ls = []
def recur_find_dir(f_path):
    folder_files = os.listdir(f_path)
    if len(folder_files) ==0:
        return
    for ff in folder_files:
        ff_path = f_path + '/' +ff
        if os.path.isfile(ff_path):
            ret_ls.append(ff)
        else:
            ret_ls.append(ff)
            recur_find_dir(ff_path)
    return

# pth = '/home/nsl3/Documents/question-set-emon/nsl-ra-evaluation-stage-1/ra_evaluation_emon/test'
pth = input('Please enter the directory path ')
recur_find_dir(pth)
print(ret_ls)