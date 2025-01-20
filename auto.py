import os 
import shutil

#Create a new directory
if not os.path.isdir("Test_directory"):
    os.mkdir("test_directory")

#Change the current working directory to the new directory
os.chdir("test_directory")
print("Current working directory: ", os.getcwd())

#Create a text file in the directory
with open("example.txt", "w") as file:
    file.write("This is a text file.")

#list files in the current directory
print("Files in the directory:", os.listdir())

#Copy the file
shutil.copy("example.txt", "copy_example.txt")

#Move the copied filke to a new location(renaming it in the process)
shutil.move("copy_example.txt", "../moved_example.txt")

#Go back to the parent directory
os.chdir("..")
#Remove the test directory and its content
shutil.rmtree("test_directory")
os.remove("moved_example.txt") #remove the moved file
print("Cleanup completed!")

import subprocess
import os
# result=subprocess.run(["echo","hello, world"],capture_output=True,text=True)
# print("command output", result.stdout)
command=["Is"]if os.name !="nt" else ["dir"]
result=subprocess.run(command,capture_output=True,text=True,shell=True)
print("files in current directory:")
print(result.stdout)

#check for error (e.g.,invalid command)
result=subprocess.run(["fake_command"],capture_output=True,text=True)
if result.returncode !=0:
    print("error",result.stderr)


import os
import shutil

#Define the directory to organiize
directory = "./example_directory"

#Create the directory and some text files
os.makedirs(directory, exist_ok=True)
with open(os.path.join(directory, "file1.txt"), "w") as f:
    f.write("Text file content")
with open(os.path.join(directory, "file2.txt"), "w") as f:
    f.write("Image file content")
with open(os.path.join(directory, "file3.txt"), "w") as f:
    f.write("Audio file content")

#Function to organize files by type
def organize_files_by_type(directory):
    #Get a list of all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        #Skip directories
        if os.path.isdir(file_path):
            continue
        #Get the file extension
        file_extension = file_name.split(".")[-1]
        #Create a folder for the file type f it doesnot exist
        type_folder = os.path.join(directory, file_extension)
        os.makedirs(type_folder, exist_ok=True)
        #Move the file to the appropriate folder
        shutil.move(file_path, os.path.join(type_folder, file_name))
        print(f"Moved {file_name} to {type_folder}/")

#Call the functioin
organize_files_by_type(directory)

#Display organized structure

for root, dirs, files in os.walk(directory):
    print(f"\nIn {root}:")
    for dir_name in dirs:
        print(f"Directory: {dir_name}")
    for file_name in files:
        print(f"Directory: {file_name}")

#Clean up
#shutil.rmtree(directory)