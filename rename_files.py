import os

def rename_files():

    #(1) get file names from a folder
    file_list=os.listdir('/Users/yunsongli/Desktop/prank')
    print (file_list)
    saved_path=os.getcwd()
    print("original working directory is " +saved_path)
    os.chdir('/Users/yunsongli/Desktop/prank')
    
    #(2) for each file, rename filename
    # string.translate(table which translate one set of characters to another set, list of characters to remove)
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,'0123456789'))
    os.chdir(saved_path)
    
rename_files()
