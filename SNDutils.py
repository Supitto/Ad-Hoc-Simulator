import json

def getJSON(path):
    print("recovering "+path)
    bufferFile = open(path,'r')
    config =  json.loads(bufferFile.read())
    bufferFile.close()
    return config