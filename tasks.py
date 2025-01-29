# #deque
# from collections import deque
# task = deque(['go to college','eat food', 'do your task'])
# task2 = task.append('go to the shop')
# print(task)
# task.remove('eat food')
# print(task)
# task.rotate

# #Collections module
# #Counter
# from collections import Counter
# paragraph = """This is a sample paragraph. This paragraph is just a simple example 
# to demonstrate how to count word frequency using Python."""   
# words = paragraph.lower().split()
# word_count = Counter(words)
# top_words = word_count.most_common
# print("Top 3 most common words:")
# print(f"{words}:{Counter}")

# #defaultdict
# from collections import defaultdict
# inventory = defaultdict(list)
# def add_product(category, product):
#     inventory[category].append(product)
#     print(f"Added {product} to category {category}")
# def display_inventory():
#     print("\nCurrent Inventory:")
#     for category, product in inventory.items():
#         print(f"{category}: {','.join(product)}") 
#     print()
# #Example usages
# add_product("Clothing", "T-Shirt")
# add_product("Electronics", "Smartphone")
# add_product("Electronics", "Smartwatch")
# add_product("Electronics", "TV")
# add_product("Clothing", "Pants")
# display_inventory()

# #Numpy
# #Basic array
# import numpy as np
# array = np.array([10, 20, 30, 40, 50])
# array_sum = np.sum(array)
# array_mean = np.mean(array)
# array_std = np.std(array)
# array_multiplied = array*2
# print("Original Array:", array)
# print("Sum of elements:", array_sum)
# print("Mean of elements:", array_mean)
# print("Standard Deviation:", array_std)
# print("Array after multiplying each element by 2:", array_multiplied)

# #Matrix Multiplication
# import numpy as np
# array1 = np.array([[1,2,3,], [4,5,6]])
# array2 = np.array([[7,8], [9,10], [11,12]])
# result = np.dot(array1, array2)
# print("Array 1;")
# print(array1)
# print("\nArray 2:")
# print(array2)
# print("\nMatrix Multiplication Result:")
# print(result)

# #CSV/Excle
# #Read and Process CSV
# import csv
# data_path = "employees.csv"

# def create_csv():
#     headers = ["Name", "Age", "Department",]
#     with open(data_path, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(headers)
#     print("File has been created.")

# def add_data(Name, Age, Department):
#     with open(data_path, mode = "a", newline = "") as file:
#         writer = csv.writer(file)
#         writer.writerow([Name, Age, Department])

# def read_csv():
#     with open(data_path, mode="r") as file:
#         reader = csv.DictReader(file)
#         print("\nEmployees older than 30:")
#         for row in reader:
#             name = row["Name"]
#             age = int(row["Age"])
#             if age > 30:
#                 print(name)
# create_csv()
# add_data("Roshna", 100, "Finance")
# add_data("Salina", 35, "Marketing")
# add_data("Prakriti", 39, "IT department")
# add_data("Ashmita", 19, "Production")
# add_data("Roar", 29, "HR")

# read_csv()

# #Openpyxl
# import openpyxl
# student_file_path = "results.xlsx"

# def create_messy_dataset(student_file_path):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "Students Grades"

#     sheet.append(["Student Name", "Grade"])
#     sheet.append(["Roshna", "A"]) 
#     sheet.append(["Salina", "B+"])
#     sheet.append(["Prakriti", "A-"])
#     sheet.append(["Ashmita", "B"])
#     sheet.append(["Roar", "A+"])

#     workbook.save(student_file_path)
#     print(f"Dataset created and saved to '{student_file_path}'.")

# create_messy_dataset(student_file_path)

# #HTTP Requests
# #GET Request
# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         posts = response.json()

#         print("Titles of the first 5 posts:")
#         for i, post in enumerate(posts[:5], start=1):
#             print(f"{i}. {post['title']}")
#     else:
#         print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
# except requests.RequestException as e:
#     print(f"An error occurred: {e}")

# #jan 20 tasks
# #Creating a Zip file
# import os
# import shutil
# from datetime import datetime

# def backup_directory(directory_path):
#     if not os.path.exists(directory_path):
#         print(f"The directory '{directory_path}' does not exist.")
#         return
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     backup_name = f"backup_{timestamp}"
#     directory_path = os.path.abspath(directory_path)
#     output_dir = os.path.dirname(directory_path)
#     try:
#         backup_path = shutil.make_archive(
#             base_name=os.path.join(output_dir, backup_name), 
#             format='zip', 
#             root_dir=directory_path
#         )
#         print(f"Backup created successfully: {backup_path}")
#     except Exception as e:
#         print(f"Error creating backup: {e}")

# if __name__ == "__main__":                          
#     directory_to_backup = input("Enter the directory path to back up: ").strip()
#     backup_directory(directory_to_backup)

# ############
# import datetime
# import os
# import shutil
# def create_backup(source_directory):
#     if not os.path.exists(source_directory):
#         print(f"Error: The directory '{source_directory} does not exist.")
#         #Gnerate a timestamped backup name
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         backup_name = f"backup_{timestamp}"
#    #Create 
#     shutil.make_archive(backup_name, 'zip',directory_path)
#     print(f"backup created:{backup_name}.zip")
# # Example usage
# create_backup("./example_directory")


# import smtplib
# import pandas as pd
# import datetime as dt
# import schedule
# import time

# # Load birthday data from CSV
# def load_birthdays(file_path):
#     return pd.read_csv(file_path)

# # Check today's birthdays
# def check_birthdays(birthday_data):
#     today = dt.datetime.now()
#     today_str = today.strftime("%m-%d")  # Format as MM-DD
#     return birthday_data[birthday_data['Birthday'].str.contains(today_str)]

# # Send email
# def send_email(to_email, subject, body):
#     try:
#         # Your email credentials
#         sender_email = "your_email@example.com"
#         sender_password = "your_password"

#         # Connect to the email server
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()  # Secure the connection
#             server.login(sender_email, sender_password)
#             # Email content
#             message = f"Subject: {subject}\n\n{body}"
#             server.sendmail(sender_email, to_email, message)
#             print(f"Email sent to {to_email}")
#     except Exception as e:
#         print(f"Error sending email to {to_email}: {e}")

# # Main task to check birthdays and send emails
# def birthday_email_task():
#     try:
#         birthday_data = load_birthdays("birthdays.csv")
#         today_birthdays = check_birthdays(birthday_data)
        
#         if not today_birthdays.empty:
#             for _, row in today_birthdays.iterrows():
#                 name = row['Name']
#                 email = row['Email']
#                 body = f"Hi {name},\n\nWishing you a very Happy Birthday! 🎉🎂 Have a fantastic day!\n\nBest Wishes,\n[Your Name]"
#                 send_email(email, "Happy Birthday!", body)
#         else:
#             print("No birthdays today.")
#     except Exception as e:
#         print(f"Error in task: {e}")

# # Schedule the task to run daily at 8:00 AM
# schedule.every().day.at("08:00").do(birthday_email_task)

# # Keep the script running
# print("Birthday Email Automator is running...")
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Wait a minute before checking the schedule again

#Design a simple to-do list with an AQL database
import sqlite3
connection = sqlite3.connect