# ======================
# Alinadb 1.0
# By Amit Barman
# ======================
import json
import os
import hashlib

class AlinaDB(object):
    def __init__(self , location):
        os.chdir("databases")
        self.location = os.path.expanduser(location+".json")
        self.load(self.location)

    # Authentication user
    def auth(self, userpass):
        try:
            creed = json.load(open(self.location, "r"))
            user_data = creed[self.hash_creds(userpass)]
            return user_data
        except:
            return 'False'

    # load db json file
    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    # add user
    def create_user(self , key , value):
        try:
            curr_db = self.location.split(".")
            self.change_db("users")
            self.insert(key, value)
            self.change_db(curr_db[0])
            return True
        except:
            return False

    # change current database
    def change_db(self, location):
        self.location = os.path.expanduser(location+".json")
        self.load(self.location)

    # read data from json file
    def _load(self):
        self.db = json.load(open(self.location , "r"))

    # dump/alter on db
    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    # function for list database
    def show_db(self):
        dbs = os.listdir()
        print("  +-----------------------+")
        print("+-| Databases             |")
        print("| +-----------------------+")
        print("|")
        print("+------o")
        count = 0
        for db in dbs:
            if ".json" in db:
                db_name = db.split('.')
                print(f"        {db_name[0]}")
                count += 1
        print(f"\n{count} rows in set")

    # create subsets
    def create_subset(self, key):
        try:
            if(self.get(key)):
                print("Key you enter is all ready exist")
            else:
                self.db[str(key)] = {}
                self.dumpdb()
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))

    # insert value on database
    def insert(self , key , value):
        try:
            if(self.get(key)):
                print("key you enter all ready exist")
            else:
                self.db[str(key)] = value
                self.dumpdb()
                return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    # insert on subsets
    def insert_on_subset(self, subset, key, value):
        if self.find_subset(subset):
            if key in self.db[subset]:
                print("key you enter all ready exist")
            else:
                self.db[subset][str(key)] = value
                self.dumpdb()
                return True
        else:
            return False

    # show/get values from database
    def get(self , key):
        try:
            print(f"[{key}] o-.--> ({self.db[key]})")
            return True
        except KeyError:
            print("No Value Can Be Found for " + str(key))
            return False

    # update value on database
    def update_values(self, key, value):
        try:
            if(self.db[key]):
                if "{" not in str(self.db[key]):
                    self.db[str(key)] = value
                    self.dumpdb()
        except Exception as e:
            print("[X] Error updating Values to Database : " + str(e))

    # update value on subsets
    def update_values_subset(self, subset, key, value):
        if self.find_subset(subset):
            self.db[subset][str(key)] = value
            self.dumpdb()

    #show all subsets
    def get_all_subset(self):
        db_data = json.load(open(self.location , "r"))
        count = 0
        for subsets in db_data:
            sets = str(db_data[subsets])
            if "{" in sets:
                print(subsets)
                count += 1
        print(f"{count} subsets found")

    # get single value form given key
    def get_value_with_key(self, s_key, val_key):
        try:
            db_data = json.load(open(self.location , "r"))
            for sub_key in db_data:
                if s_key == sub_key:
                    print(f"[{sub_key}]--->({val_key})o-.-->{db_data[s_key][val_key]}")
        except:
            return False

    # function for find subsets
    def find_subset(self, key):
        db_data = json.load(open(self.location , "r"))
        for key_value in db_data:
            if key == key_value:
                return True
        return False

    # show all entryes on database
    def show_all(self):
        try:
            db_data = json.load(open(self.location , "r"))
            count = 0
            for key in db_data:
                if "{" not in str(db_data[key]):
                    print(f"{key} o---> {db_data[key]}\n")
                else:
                    print(f"+-[{key}]")
                    print(f"|")
                    print(f"+-----------> {db_data[key]}\n")
                count += 1
            print(f"{count} rows in set")
        except:
            return False

    # get all from one subset
    def show_all_from_subset(self, key):
        try:
            db_data = json.load(open(self.location , "r"))
            count = 0
            for sub_key in db_data:
                if key == sub_key:
                    print(f"+--[{key}]~[set]")
                    print(f"|")
                    print(f"+------>")
                    set_data = db_data[key]
                    for data in set_data:
                        print(f"       {data} o----> {set_data[data]}")
                        count += 1
            print(f"\n{count} rows found")
        except:
            return False

    # hashing username and password
    def hash_creds(self, userpass):
        result = hashlib.md5()              # md5 hash
        result.update("s4lt3d".encode())    # salting password
        result.update(userpass.encode())    # hash password with salt string
        return result.hexdigest()

    # delete value from database
    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

     # delete data from subset
    def delete_from_subset(self, subset, key):
        if not subset in self.db:
            return False
        else:
            del self.db[subset][key]
            self.dumpdb()
            return True

    # delete database
    def delete_db(self, db_name):
        try:
            os.remove(db_name+".json")
            print(f"{db_name} successfully deleted")
        except:
            print("Unable to delete databases!")

    # version of database
    def version(self):
        print("AlinaDB v1.0")

    # function for show help
    def help(self):
        print("+========================================================+")
        print("| AlinaDB v1.0                                           |")
        print("| By Amit Barman                                         |")
        print("+========================================================+")
        print("insert <key> <data> \t\t insert/add data on Database")
        print("delete <key> \t\t\t delete/remove data for Database of given key")
        print("get <key> \t\t\t Show value of given key")
        print("show all \t\t\t Show all data on Database")
        print("show dbs \t\t\t for show all Databases")
        print("version \t\t\t Show version")
        print("use <db_name>\t\t\t change/create Database")
        print("add user <user_name> <password> <privileges>('all' for give all priveleges)")
        print(" \t\t\t\t create new users on Database")
        print("*Note : user privelege type r = read only, w = write, and x = create users")
        print("show privelege \t\t\t show current user priveleges")
        print("get all from <subset_name> \t for get all value from subset")
        print("create <subset_name> \t\t create a subset into current Database")
        print("get from <subset_name> <key> \t get value for given key from subset")
        print("show all subset \t\t show all subsets in current Database")
        print("quit or exit \t\t\t for exiting Database program")
        print("help \t\t\t\t List all AlinaDB commands\n")