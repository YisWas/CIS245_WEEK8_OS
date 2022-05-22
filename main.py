import os

selected_dir = input("Enter a directory: ") #getting a directory
while not os.path.isdir(selected_dir): #checking that its a valid directory
    selected_dir = input("Please enter a valid directory: ")
file_name = input("Enter new file's name: ")
file_path = os.path.join(selected_dir, file_name) #making the path by adding the name and directory

name = input("Enter your name: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")

with open(file_path, "w") as f: # "w" is writing in the file
    f.write(name + "," + address + "," + phone) #writing the file and adding "," to make it comma sepertaed
with open(file_path, "r") as f: #"r" is to read the file
    print("Validating file...")
    print(f.read())  #printing the file