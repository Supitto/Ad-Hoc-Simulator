"""Main script of Generate-N-Deploy"""
import os
import dockerfile
import time


opt = -1
basePath = "./build/"

while opt != 0:
    print("Welcome to G-N-D")
    print("What do you want today?\n")
    print("1 - Generate DockerFile")
    print("2 - Manage APT packs")
    print("3 - Change build path")
    print("0 - To Exit")
    try:
        opt = int(input("option : "))
    except:
        print("Invalid option")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')