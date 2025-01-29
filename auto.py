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

# #Call the functioin
# organize_files_by_type(directory)

# #Display organized structure

# for root, dirs, files in os.walk(directory):
#     print(f"\nIn {root}:")
#     for dir_name in dirs:
#         print(f"Directory: {dir_name}")
#     for file_name in files:
#         print(f"Directory: {file_name}")
#Clean up
#shutil.rmtree(directory)
#################################################################
# import subprocess
# import os
# def list_running_process(output_file):
#      try:
#         command=['tasklist'if os.name=='nt'else['ps','aux']]
#         result=subprocess.run(command,captutre_output=True,text=True)
#         with open(output_file,'w')as file:
#             file.write(result.stdout)
#         print(f"process list saved to '{output_file}'")
#      except Exception as e:
#         print(f"error:{e}")
# list_running_process("process_list.txt")
###############
#File Cleanup Bot
import os
import shutil
from datetime import datetime, timedelta

def file_cleanup(directory, days):
    archive_folder = os.path.join(directory, "Archive")
    os.makedirs(archive_folder, exist_ok=True)
    cutoff_date = datetime.now() - timedelta(days=days)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_mtime < cutoff_date:
                shutil.move(file_path, archive_folder)
                print(f"Moved: {filename}")
    confirm = input(f"Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
    if confirm == 'yes':
        shutil.rmtree(archive_folder)
        print("Archive folder deleted.")
    else:
        print("Archive folder retained.")

# Example usage
file_cleanup('/path/to/directory', 30)  

##########################################
#System Diagnostics Report
import os
import platform
import subprocess

def system_diagnostics_report(output_file):
    cwd = os.getcwd()
    disk_usage = subprocess.getoutput(f"du -sh {cwd}")
    os_info = platform.uname()
    report = f"""
System Diagnostics Report
==========================
Current Working Directory: {cwd}

Disk Usage:
{disk_usage}

System Information:
- System: {os_info.system}
- Node Name: {os_info.node}
- Release: {os_info.release}
- Version: {os_info.version}
- Machine: {os_info.machine}
- Processor: {os_info.processor}
"""
    with open(output_file, "w") as file:
        file.write(report)

    print(f"Report saved to {output_file}")
# Usage
output_file = input("Enter the file path to save the report (e.g., diagnostics.txt): ")
system_diagnostics_report(output_file)
import os
import shutil
import subprocess

def generate_system_report(output_file):
    try:
        # Get current working directory
        cwd = os.getcwd()

        # Get disk usage of the current directory
        disk_usage = shutil.disk_usage(cwd)

        # Get system information
        system_info = subprocess.run(['systeminfo'], capture_output=True, text=True).stdout

        # Write the report to a file
        with open(output_file, 'w') as file:
            file.write(f"Current Working Directory: {cwd}\n")
            file.write(f"Disk Usage:\n")
            file.write(f"  Total: {disk_usage.total / (1024 ** 3):.2f} GB\n")
            file.write(f"  Used: {disk_usage.used / (1024 ** 3):.2f} GB\n")
            file.write(f"  Free: {disk_usage.free / (1024 ** 3):.2f} GB\n")
            file.write(f"System Information:\n{system_info}\n")

        print(f"System diagnostics report saved to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

# # Example usage
# generate_system_report("system_report.txt")
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
#Email Credentials
sender_email = "ashmitashrestha613@gmail.com"
receiver_email = "ruman.metahorizon@gmail.com"
password = "iwya aaoz tpho ekti"
#Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"
#Email body
body = "Hello, this is a test email sent from python."
message.attach(MIMEText(body, "plain"))
#Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail (sender_email, receiver_email, message.as_string())
    print("Email sent sucessfully!")    
except Exception as e:
    print(f"Error: {e}")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#email credentials
sender_email="ashmitashrestha613@gmail.com"
recevier_email="ruman.metahorizon@gmail.com"
password="iwya aaoz tpho ekti"
message=MIMEMultipart()
message["from"]=sender_email
message["to"]=recevier_email
message["subject"]="test email"
body="hello, this is a test email send from python"
message.attach(MIMEText(body,"plain"))
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,recevier_email,message.as_string())
    print("emeil sent successfully!")
except Exception as e:
    print(f"error:{e}")
 
#
import sqlite3
connection=sqlite3.connect("store.db")
cursor=connection.cursor()
# Create a table of products
cursor.execute('''CREATE TABLE IF NOT EXISTS products(
               id INTEGER Primary Key,
               name TEXT NOT NULL,
               price REAL NOT NULL)'''
               )
# Insrt data
cursor.execute("INSERT INTO products(name,price)VALUES(?,?)",("Laptop",999.999))
connection.commit()

#Using SQLAlchemy for database interaction 
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

#Create engine and session
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
#Add a new product
new_product = Product (name="Tablet", price=299.99)
session.add(new_product)
session.commit()
#Query products
for product in session.query(Product):
    print(product.name, product.price)
#Task 1
import sqlite3
connection = sqlite3.connect("Book.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL
)
''')
cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Life or Death", "Ashmita Shrestha", 600.23))
cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Life on Verge", "APM on Line", 700.23))
cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Hello from Other side", "lilly", 400))
connection.commit()
cursor.execute("SELECT * FROM book")
for row in cursor.fetchall():
    print(row)
connection.close()

#todolist
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ToDoList(Base):
    __tablename__ = 'todolist'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    due_date=Column(String,nullable=False)

engine = create_engine('sqlite:///mytodolist.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_todolist_1=ToDoList(description="Make  bed",due_date=2)
new_todolist_2=ToDoList(description="Wash Clothes",due_date=3)
new_todolist_3=ToDoList(description="Do dishes",due_date=3)

session.add(new_todolist_1)
session.add(new_todolist_2)
session.add(new_todolist_3)
session.commit()
session.delete(new_todolist_3)
session.commit()

for todolist in session.query(ToDoList):
    print(todolist.description,todolist.due_date)

#task- 2
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Store(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    genre=Column(String,nullable=False)
    author=Column(String,nullable=False)
    rating=Column(Integer,nullable=False)

engine = create_engine('sqlite:///favourites.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_book1=Store(genre="Horror",author="Ray Mon",rating=3.5)
new_book2=Store(genre="RomCom",author="Helena",rating=5)
new_book3=Store(genre="Anime",author="My",rating=2.1)
new_book4=Store(genre="Self-development",author="Richard ho",rating=4.1)
session.add_all([new_book1,new_book2,new_book3,new_book4])
session.commit()
session.delete(new_book3)

def search_book(search_author):
    books= session.query(Store).filter(Store.author==search_author).first()
    if books:
        print(f"Book is Found{books.genre} ,{books.author} and rating{books.rating}")

    
    else:
        print("Book is not found")
search_author="Helena"
search_book(search_author)