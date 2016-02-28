import fileinput
import os.path

#This program strips the name from our userdata text file 
#to anonymize it. It also removes any distabled accounts. 
#=========================================
#holds all the data from userdata. 
filename = "userdata.txt"
saveToFileName = "clean_userdata.txt"
#List that holds all our userdata
userDataList = []
#Holds are cleaned up data.
cleanUserDataList = []

headerString = 'Page Visits\tSubmissions\tComments Received\tComments Given\tJournals\tFavs'
matchString = 'Profile is disabled'

#=========================================
#Checking to see if our file exists. 
doesFileExist = os.path.isfile(filename)
if doesFileExist == True:
	print "userdata.txt opened"
	with open(filename) as file:
		userDataList = file.read().splitlines()
		file.close()

elif doesFileExist == False:
	sys.exit("Userdata file does not exist, quitting")

else:
	sys.exit("Something blew up when making the file")


#Adding header just to make it easy to read. 
cleanUserDataList.append(headerString)

for users in userDataList:
	head, sep, tail = users.partition('\t')
	if(tail != matchString):
		cleanUserDataList.append(tail)

saveFile = open(saveToFileName, 'w')
saveFile.write("\n".join(cleanUserDataList))
saveFile.close()
