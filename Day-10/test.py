import os

folders = input("please provide folders name with spaces in betweeen :-  ").split()

for folder in folders:
    print("--------listing files for folder---" + folder)

    try:
      files=os.listdir(folder)
    except FileNotFoundError:
       print("please provide a valid folder Name looks like this folder doesn't exists :- " + folder)
       continue
    except PermissionError:
        print("User doesn't have autherization for the folder :- " + folder)
        continue
    for file in files:
        print(file)