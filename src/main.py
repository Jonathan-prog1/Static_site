import os
import shutil
from copystatic import copy_files_recursive
def main():

    public = "public"
    static = "static"
    
    
    

    # Checks to see if the user has the public folder
    if os.path.exists(public) != True:
        print("Crateing the public directory")
        os.mkdir("public")
        
    elif os.path.exists(public):
        try:
            shutil.rmtree(public)
            print(f"{public} Directory and its contents have been deleted.")
            os.mkdir("public")
            print(f"The {public}: Directory has been created.")
        except Exception as e:
            print(f"Error deleting directory '{public}': {e}")

                
    
    copy_files_recursive(static , public)
    

    
       
  
main()
