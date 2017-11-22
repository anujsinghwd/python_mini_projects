import os;
def rename_files():
    file_list = os.listdir("C:\Users\BALMUKUND\Downloads\prank");

    save_path = os.getcwd();
    os.chdir("C:\Users\BALMUKUND\Downloads\prank");
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"));
    os.chdir(save_path);
    
rename_files()    
    
