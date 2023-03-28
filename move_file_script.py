secondary_build_location = sr.Get_Shared_Variables("secondary_build_location") # input data
moved_secondary_build_location = sr.Get_Shared_Variables("secondary_buil_move_location") # input data



import os
import glob
import pathlib


source = secondary_build_location
destination = moved_secondary_build_location


dir_path = source
exe_file_name = glob.glob(dir_path + '/*.exe')

if exe_file_name != []:

    acquire_build_name = exe_file_name[0].split('\\')[-1].replace('.exe','').strip()
    new_path = pathlib.Path(destination + '\\' + acquire_build_name)
    new_path.mkdir(parents=True, exist_ok=True)
    allfiles = os.listdir(source)

    # #iterate on all files to move them to destination folder
    for f in allfiles:
        src_path = os.path.join(source, f)
        dst_path = os.path.join(new_path, f)
        os.rename(src_path, dst_path)
else:
    pass
