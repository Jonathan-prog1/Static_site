from textnode import TextNode,TextType
import os
import shutil
def main():

    public = "public"
    static = "static"
    
    
    

    # Checks to see if the user has the public folder
    if os.path.exists(public) != True:
        try:
            os.mkdir("public")
        except FileExistsError:
            print("Directory already exists.")
    elif os.path.exists(public):
        try:
            shutil.rmtree(public)
            print(f"{public} Directory and its contents have been deleted.")
            os.mkdir("public")
            print(f"The {public}: Directory has been created.")
        except Exception as e:
            print(f"Error deleting directory '{public}': {e}")
     
    def copy_static_to_public(source_dir, dest_dir):
    # Create destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
        
        # Get all items in the source directory
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            dest_path = os.path.join(dest_dir, item)
        
            # Check if it's a file
            if os.path.isfile(source_path):
                # Copy the file
                print(f"Copying file: {source_path} to {dest_path}")
                shutil.copy(source_path, dest_path)
            # If it's a directory, recursively copy it

            else:
                # Create the directory in destination
                print(f"Creating directory: {dest_path}")
                if not os.path.exists(dest_path):
                    os.mkdir(dest_path)
                # Recursively copy contents of this directory
                copy_static_to_public(source_path, dest_path)
    
    copy_static_to_public(static, public)
    

    
       
  
main()
