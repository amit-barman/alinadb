# ======================
# Alinadb 1.0
# By Amit Barman
# ======================
import Alinadb
import getpass

if __name__ == "__main__":
    obj = Alinadb.AlinaDB("users")
    user = input("Enter user name : ")
    password = getpass.getpass(prompt="Enter password : ")
    privilege = obj.auth(f"{user}:{password}")
    if 'False'not in privilege:
        user_db = input("[AlinaDB]Enter Database name you want to use/create : ")
        obj.change_db(user_db)
        exit = False
        while not exit:
            command = input("["+user_db+"]"+">> ")
            arr = command.split(" ")
            try:
                if len(arr) >= 1:
                    if arr[0] == "insert" and len(arr) == 3 and 'w' in privilege:
                        obj.insert(arr[1], arr[2])
                    elif arr[0] == "create" and len(arr) == 2 and 'w' in privilege:
                        obj.create_subset(arr[1])
                    elif arr[0] == "insert" and arr[1] == "into" and len(arr) == 5 and 'w' in privilege:
                        obj.insert_on_subset(arr[2], arr[3], arr[4])
                    elif arr[0] == "delete" and len(arr) == 2 and 'w' in privilege:
                        obj.delete(arr[1])
                    elif arr[0] == "delete" and arr[1] == "from" and len(arr) == 4 and 'w' in privilege:
                        obj.delete_from_subset(arr[2], arr[3])
                    elif arr[0] == "get" and len(arr) == 2:
                        obj.get(arr[1])
                    elif arr[0] == "get" and arr[1] == "all" and arr[2] == "from" and len(arr) == 4:
                        obj.show_all_from_subset(arr[3])
                    elif arr[0] == "get" and arr[1] == "from" and len(arr) == 4:
                        obj.get_value_with_key(arr[2], arr[3])
                    elif arr[0] == "show" and arr[1] == "all" and len(arr) == 2:
                        obj.show_all()
                    elif arr[0] == "show" and arr[1] == "all" and arr[2] == "subsets" and len(arr) == 3:
                        obj.get_all_subset()
                    elif arr[0] == "show" and arr[1] == "dbs" and len(arr) == 2:
                        obj.show_db()
                    elif arr[0] == "update" and len(arr) == 3:
                        obj.update_values(arr[1], arr[2])
                    elif arr[0] == "update" and arr[1] == "into" and len(arr) == 5:
                        obj.update_values_subset(arr[2], arr[3], arr[4])
                    elif arr[0] == "use" and arr[1] != "users" and len(arr) == 2:
                        print(f"changing to {arr[1]}...")
                        user_db = arr[1]
                        obj.change_db(arr[1])
                    elif arr[0] == "add" and arr[1] == "user" and len(arr) == 5 and 'x' in privilege:
                        if arr[4] == "all":
                            obj.create_user(obj.hash_creds(arr[2]+':'+arr[3]), "rwx")
                        else:
                            obj.create_user(obj.hash_creds((arr[2]+':'+arr[3])), arr[4])
                    elif arr[0] == "show" and arr[1] == "privilege" and len(arr) == 2:
                        print(privilege)
                    elif arr[0] == "version" and len(arr) == 1:
                        obj.version()
                    elif arr[0] == "help" and len(arr) == 1:
                        obj.help()
                    elif arr[0] == "delete" and arr[1] == "database" and len(arr) == 3:
                        obj.delete_db(arr[2])
                    elif arr[0] == "exit" or arr[0] == "quit" and len(arr) == 1:
                        print("Bye Bye ^_^")
                        exit = True
                    else:
                        print("You have enter an invalid AlinaDB comand")
                        print("for see comands list type 'help'")
                else:
                    print("[-] please enter a valid number of arguments")
            except:
                print("invalid aql(alina query languige) query")
    else:
        print("You have enter an invalid username or password!")
# End
