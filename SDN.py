"""Main menu of Generate-N-Deploy"""


from SNDutils import getJSON
import os
import manager

basePath = os.path.dirname(os.path.abspath(__file__))
paths = getJSON(basePath+"/paths.json")

opt = ""

def build():
    print("Not implemented, come back later")

def manage():
    man = manager.Manager(paths["config"],paths["help"])
    man.console()

def simulate():
    print("Not implemented, come back later")

def deploy():
    print("Not implemented, come back later")

def config():
    print("Not implemented, come back later")

def help_screen():
    help_file = open(paths["help"]+'main.help','r')
    print(help_file.read())
    help_file.close()

print("Welcome to S-N-D")
print("What do you want today?\n")
while opt != "quit":
    try:
        opt = str(input("(type help for help) >> "))
    except EOFError:
        print("Got EOF")
        opt = "quit"
    
    if opt == 'quit':
        print("Good bye, didn't liked you anyway")
    elif opt == 'help':
        help_screen()
    elif opt == 'build':
        build()
    elif opt == 'manage':
        manage()
    elif opt == 'simulate':
        simulate()
    elif opt == 'deploy':
        deploy()
    elif opt == 'config':
        config()
    else:
        print("Option not recognized, you moron")
    print("")

