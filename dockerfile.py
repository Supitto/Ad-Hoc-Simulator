import json

class Dockerfile:
    basePath="./"
    def __init__(self, path="./"):
        global basePath
        basePath = path

    def getDockeFileString(self):
        return ""

    def getJSON(self, path):
        print("recovering "+basePath+path)
        bufferFile = open(basePath+path,'r')
        config =  json.loads(bufferFile.read())
        bufferFile.close()
        return config

    def isTrue(self,statement):
        if statement == "True" or statement == "true" or statement == "t" or statement == "T":
            return True
        return False

    def WriteFile(self):
        endFile = open(basePath+"dockerfile",'w')
        #dockerfile header
        print("Making dockerfile header ....")
        image_config = self.getJSON("config/image_config.json")
        endFile.write("FROM "+image_config["base-image"]+":"+image_config["base-image-tag"]+"\n" )
        endFile.write("LABEL maintainer=\""+image_config["maintainer"]+"\"\n" )
        #making APT work
        print("Making dockerfile apt session ...")
        apt_config = self.getJSON("config/apt_config.json")
        endFile.write("ADD [\"config/"+apt_config["source-path"]+"sources.list"+"\", \"/etc/apt/\"]\n")
        if(self.isTrue(apt_config["update"])):
            endFile.write("RUN apt-get update -y \n")
        if(self.isTrue(apt_config["upgrade"])):
            endFile.write("RUN apt-get upgrade -y \n")
        for pack in apt_config["package-list"]:
            endFile.write("RUN apt-get install -y "+str(pack["name"])+"\n")
        endFile.write("CMD bash")
        endFile.close()

