
class Manager:

    configPath = ""
    helpPath = ""

    def __init__(self,config_path, help_path):
        global helpPath
        global configPath
        configPath = config_path
        helpPath = help_path
        print("Starting manager using "+configPath+" as base path for configs")
    
    def help_screen(self):
        global helpPath
        help_file = open(helpPath+'manager.help','r')
        print(help_file.read())
        help_file.close()

    def console(self):
        print("You are now in the manager module, be happy")
        print("What do you want\n")
        opt = ""
        while opt != "quit":
            try:
                opt = str(input("(type help for help) >> "))
            except EOFError:
                print("Got EOF")
                opt = "quit"
            if opt == "quit":
                print("Goodbye sucker")
            elif opt == "dependencies":
                print("Still not implemented")
            elif opt == "properties":
                print("Dont tweak me like that senpai")
            elif opt == "help":
                self.help_screen()
            else:
                print("Your typo is so uggly that i cant even recognize what you want")
            print("")