import os
import shutil
from copystatic import copy_files_recursive
from page_generator import generate_pages_recursive
def main():

    dir_path_static = "./static"
    dir_path_public = "./public"
    dir_path_content = "./content"
    template_path = "./template.html"
    
    
    

    # Checks to see if the user has the public folder
    if os.path.exists(dir_path_public) != True:
        print("Crateing the public directory")
        os.mkdir("public")
        
    elif os.path.exists(dir_path_public):
        try:
            shutil.rmtree(dir_path_public)
            print(f"{dir_path_public} Directory and its contents have been deleted.")
            os.mkdir("public")
            print(f"The {dir_path_public}: Directory has been created.")
        except Exception as e:
            print(f"Error deleting directory '{dir_path_public}': {e}")

                
    
    copy_files_recursive(dir_path_static , dir_path_public)
    
     
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
       
if __name__ == "__main__": 
    main()
