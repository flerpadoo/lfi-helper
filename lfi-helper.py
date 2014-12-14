#!/usr/bin/python
import urllib2
baseURL = ""
def getBaseURL():
        global baseURL
        baseURL = raw_input("Please enter the base url you want to start in: ")
        print("You can change the base url any time by typing '!changethebaseurl' at the prompt\n"+\
        "To exit, type '!exitlfihelper'")
        return baseURL
def getFile(baseURL):
        filePath = raw_input("\nfilepath~> ")
        if filePath == "!changethebaseurl":
                baseURL = getBaseURL()
                getFile(baseURL)
        elif filePath == "!exitflihelper":
                sys.exit("Later!")
        response = urllib2.urlopen(baseURL + filePath)
        responseData = response.read()
        responseLength = response.headers['content-length']
        print("Content Length: " + str(responseLength))
        saveFilePath = str(filePath.replace("/","-").replace("\\","-"))
        if int(responseLength) < 1:
                yesNo = str(raw_input("Do you want to attempt to download the empty file? [y/n] ")).lower()
                if yesNo == "y" or yesNo == "yes":
                        file = open(saveFilePath, 'w')
                        file.write(responseData)
                        file.close()
                        print("Saved file to " + saveFilePath)
                if yesNo == "n" or yesNo == "no":
                        pass
        if int(responseLength) > 0:
                file = open(saveFilePath, 'w')
                file.write(responseData)
                file.close()
                print("Saved file to " + saveFilePath)
        getFile(baseURL)
getBaseURL()
getFile(baseURL)
