import json
import os


# getting the list of all files
def getFiles() -> list:

    # Get the list of all files and directories
    path = ""
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")
    # prints all files
    return dir_list


files = getFiles()


# getting all the eventhub names
def eventhubnames():

    file_list = files
    for a in file_list:
        with open(a, "r") as file:
            data = json.loads(file.read())
            if "aehInfo" in data:
                if "eventHubs" not in data["aehInfo"]:
                    continue
                else:
                    z = data["aehInfo"]["eventHubs"]
                    for i in range(0, len(z)):
                        names = z[i]["eventHubName"]
                        with open("eventhubs.txt", "a") as final:
                            final.write(names + "\n")
            else:
                continue


# getting all the databasesnames
def databasenames():

    file_list = files
    for a in file_list:
        with open(a, "r") as file:
            data = json.loads(file.read())
            if "adxInfo" in data:
                if "databaseName" not in data["adxInfo"]:
                    continue
                else:
                    z = data["adxInfo"]["databaseName"]
                    with open("databaseP.txt", "a") as final:
                        final.write(z + "\n")
            else:
                continue


eventhubnames()
databasenames()
