import os
from typing import re


class ModifyFileName:

    def __init__(self):
        pass

    def renameFile(self, osName):
        fileList = os.listdir(osName)
        print(fileList)
        # get current work path
        os.chdir(osName)
        # currentpath = os.getcwd()
        # print(osName)
        # print("Current is " + currentpath)
        # change current work path
        # os.chdir(r"C:\Users\dell\Desktop\Udacity\prank\prank")
        osMap = set()
        for fileName in fileList:
            # delete 0123456789 in file name
            if os.path.isdir(osName + '/' + fileName):
                osMap.add(osName + '/' + fileName)
            if fileName.startswith('0'):
                print("Original is " + fileName)
                print()
                os.rename(fileName, fileName.replace('0', '', 1))
            # os.rename(fileName, fileName.translate(None, "0123456789"))
            # print("Changed is " + fileName.translate(None, "0123456789"))
        for osName in osMap:
            self.renameFile(osName)
        # os.chdir(currentpath)


if __name__ == '__main__':
    ModifyFileName().renameFile(r"/Users/skp/PycharmProjects/my-python")
