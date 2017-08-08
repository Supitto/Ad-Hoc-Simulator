import time
import os
import json

class AptManager:
    basePath="./"
    apt_tree = {}
    def __init__(self, path="./"):
        global basePath
        basePath = path
        global apt_tree
        apt_tree = self.getJSON("apt_config.json")
    
    def getJSON(self, path):
        bufferFile = open(basePath+path,'r')
        config =  json.loads(bufferFile.read())
        bufferFile.close()
        return config
    
    def showPackagesIndex(self):
        for i in range(len(apt_tree["package-list"])):
            print(str(i)+" : "+apt_tree["package-list"][i]["name"])
    
    def removePackageFromIndex(self, index):
        del apt_tree["package-list"][index] 
    
    def removePackageFromName(self, packageName):
        apt_tree["package-list"].remove({"name":packageName})

    def addPackage(self, packageName):
        apt_tree["package-list"].append({"name":packageName})

    def editPackageFromIndex(self, index, newName):
        apt_tree["package-list"][index] = {"name":newName}
    
    def editPackageFromName(self, oldName, newName):
        apt_tree["package-list"][apt_tree["package-list"].index({"name":oldName})] = {"name":newName}
    
    def console(self):
        opt = -1
        while opt != 0:
            print("Welcome to APT-Manager")
            print("What do you want today?\n")
            print("1 - List packages")
            print("2 - Remove a package")
            print("3 - Edit a package name")
            print("4 - Add a new package")
            print("5 - Save changes")
            print("0 - To Exit")
            try:
                opt = int(input("option : "))
            except:
                print("Invalid option")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            if opt != -1:
                if opt == 1:
                    print("This is the list of packages with their indexs")
                    self.showPackagesIndex()
                    input("Press any key to go back to the menu ...")
                elif opt == 2:
                    var = input("Please type the name of the package or it index : ")
                    try:
                        if self.isInt(var):
                            self.removePackageFromIndex(int(var))
                        else:
                            self.removePackageFromName(var)
                    except:
                        print("Sorry master, I could not fulfill my duty : ")
                elif opt == 3:
                    var = input("Please type the name of the package or it index : ")
                    new = input("Please type the new name : ")
                    try:
                        if self.isInt(var):
                            self.editPackageFromIndex(int(var),new)
                        else:
                            self.editPackageFromName(var,new)
                    except:
                        print("Sorry master, I could not fulfill my duty")
                elif opt == 4:
                    name = input("Please type the name of the package : ")
                    self.addPackage(name)
                elif opt == 5:
                    print("Saving changes ...")
                    try:
                        bufferFile = open(basePath+"apt_config.json",'w')
                        config =  bufferFile.write(json.dumps(apt_tree,indent=4))
                        bufferFile.close()
                    except:
                        print("Could not save changes")
                if opt != 0:
                    opt = -1

    def isInt(self,var):
        try:
            mock = int(var)
            return True
        except:
            return False