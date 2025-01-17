#deque
from collections import deque
task = deque(['go to college','eat food', 'do your task'])
task2 = task.append('go to the shop')
print(task)
task.remove('eat food')
print(task)
task.rotate

#Collections module
#Counter
from collections import Counter
paragraph = """This is a sample paragraph. This paragraph is just a simple example 
to demonstrate how to count word frequency using Python."""
words = paragraph.lower().split()
word_count = Counter(words)
top_words = word_count.most_common
print("Top 3 most common words:")
print(f"{words}:{Counter}")

#defaultdict
from collections import defaultdict
inventory = defaultdict(list)
def add_product(category, product):
    inventory[category].append(product)
    print(f"Added {product} to category {category}")
def display_inventory():
    print("\nCurrent Inventory:")
    for category, product in inventory.items():
        print(f"{category}: {','.join(product)}") 
    print()
#Example usages
add_product("Clothing", "T-Shirt")
add_product("Electronics", "Smartphone")
add_product("Electronics", "Smartwatch")
add_product("Electronics", "TV")
add_product("Clothing", "Pants")
display_inventory()

#Numpy
#Basic array
import numpy as np
array = np.array([10, 20, 30, 40, 50])
array_sum = np.sum(array)
array_mean = np.mean(array)
array_std = np.std(array)
array_multiplied = array*2
print("Original Array:", array)
print("Sum of elements:", array_sum)
print("Mean of elements:", array_mean)
print("Standard Deviation:", array_std)
print("Array after multiplying each element by 2:", array_multiplied)

#Matrix Multiplication
import numpy as np
array1 = np.array([[1,2,3,], [4,5,6]])
array2 = np.array([[7,8], [9,10], [11,12]])
result = np.dot(array1, array2)
print("Array 1;")
print(array1)
print("\nArray 2:")
print(array2)
print("\nMatrix Multiplication Result:")
print(result)


#CSV/Excle
#Read and Process CSV
import csv
def print_employees_older_than_30(csv_file):
    with open(csv_file,'r') as file:
        reader = csv.DictReader(file)
        print("Employees older than 30")
        for row in reader:
            if int(row['age']) > 30:
                print(row['name'])
csv_file = 'employees.csv'
print_employees_older_than_30(csv_file)