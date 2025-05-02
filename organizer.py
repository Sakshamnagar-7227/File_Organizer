import os
import shutil

file_types = { #Dictionary to categorize file types
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.java', '.cpp']
}

def organized_files(target_folder):
    if not os.path.isdr(target_folder):
        print(f"Error: {target_folder} is not a valid directory.")
        return 
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder,filename) #Get the full path of the file

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False #Flag to check if file is moved

            for folder, extensions in file_types.itmes():
                if file_ext in extensions:
                    folder_path = os.path.join(target_folder, folder) #Create a folder for the file type if it doesn't exist
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, filename)) #Move the file to the corresponding folder
                    moved = True 
                    break

            if not moved:
                other_path = os.path.join(target_folder, 'Other') #Create a folder for other file types if it doesn't exist
                os.makedirs(other_path, exist_ok=True) 
                shutil.move(file_path, os.path.join(other_path,filename)) #Move the file to the 'Other' folder
    print("Files organized successfully.")

if __name__ == "__main__":
    path = input("Enter the path of the folder to organize:") #Get the path of the folder to organize
    organized_files(path)