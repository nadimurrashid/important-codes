import os

path=r"A:\TaxCalc_PDFS_Base\Base_Files\Base_Files"
destination_path = r"A:\TaxCalc_PDFS_Base\Base_Files\Modified_FFS_File"
for filename in os.listdir(path):
    split_name = filename.split('_')
    attach_name = split_name[0] + '_' + 'FFS' + '_' + split_name[1] + '.pdf'
    print(attach_name)
    my_source = path + '\\' + filename
    my_dest = destination_path + '\\' +  attach_name
    os.rename(my_source, my_dest)


path = r"A:\TaxCalc_PDFS_Base\Base_Files_RFS\Base_Files_RFS"
destination_path = r"A:\TaxCalc_PDFS_Base\Base_Files_RFS\Modified_Base_RFS_Files"
for filename in os.listdir(path):
    split_name = filename.split('_')
    attach_name = split_name[0] + '_' + 'RFS' + '_' + split_name[1] + '.pdf'
    print(attach_name)
    my_source = path + '\\' + filename
    my_dest = destination_path + '\\' +  attach_name
    os.rename(my_source, my_dest)


path = r"A:\TaxCalc_PDFS_Base\Base_Files_LS\Base_Files_LS"
destination_path = r"A:\TaxCalc_PDFS_Base\Base_Files_LS\Modified_Base_files_LS"
for filename in os.listdir(path):
    split_name = filename.split('_')
    attach_name = split_name[0] +'_' +split_name[1]+'_'+ split_name[2]+'_'+ split_name[3] + '.pdf'
    print(attach_name)
    my_source = path + '\\' + filename
    my_dest = destination_path + '\\' +  attach_name
    os.rename(my_source, my_dest)

