
def update_server_config(filepath, key, value):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    with open(filepath ,'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                 file.write(line)

filepathnew = input("please provide file path:- ")
keytoupdate = input("please provide KEY to update:- ")
valuetoupdate = input("please provide VALUE for the KEY to update:- ")

update_server_config(filepathnew,keytoupdate,valuetoupdate)
