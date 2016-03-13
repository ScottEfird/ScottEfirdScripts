import fileinput
import sys
import re
import requests
import os.path
from BeautifulSoup import BeautifulSoup
#=========================================
filename = "userlist.txt"
userDataFilename = "userdata.txt"
#Holds all our user names
masterUserList = []
#Holds all the user names we have not checked from userdata file
userDataFileList = []

#Just to make it clear, the subset of unchecked user coming from
#the two lists above are put in to the lower list. 

#TODO We can recycle one of these lists from above. Not sure that we 
#want to tho. 

#Holds all the users we have not checked yet.
uncheckedUserList = []
#Holds the data we've colected. 
userData = []
#Holds our statistic data for avgs 
pageViews = "0"
submissions = "0"
commentsReceived = "0"
commentsGiven = "0"
journals = "0"
favorites = "0"

#=========================================
#Checking to see if our username exists. 
doesFileExist = os.path.isfile(filename)
if doesFileExist == True:
	print "userlist.txt opened"
	with open(filename) as file:
		masterUserList = file.read().splitlines()
		file.close()

elif doesFileExist == False:
	sys.exit("Username file does not exist, quitting")

else:
	sys.exit("Something blew up when making the file")
#=========================================
#Opening our userdata file so we can resume our old work. 
doesUserDataFileExist = os.path.isfile(userDataFilename)
if doesUserDataFileExist == True:
	print "Found old user data, loading it in."
	#Yea yea yea, the naming sucks here. 
	with open (userDataFilename) as userDataFileList_file:
		userDataFileList = userDataFileList_file.read().splitlines()
elif doesUserDataFileExist == False:
	#Creating our file
	print "The file does not exist, creating file"
	file = open(userDataFilename, "w")
else:
	sys.exit("Something blew up when making the old user data file.")
#=========================================
#Takes in our masterUserList, userDataFileList and puts all the unchecked
#users into uncheckedUserList. 
def findUnscrapedUsers ():
	#Adding all our old saved data to our current user list
	userData = list(userDataFileList)

	print "Scraping user profiles!"
	print "-------------------------------------"
	for item in userDataFileList:
		head, sep, tail = item.partition('\t')
		uncheckedUserList.append(head)
	oldUsers = len(userData)
	print "Found "+str(oldUsers)+" old users."
	print "Loading old user data (This could take awhile)"
	print "-------------------------------------"
	return userData

#Format for the user list of statistic data. 
#------------------------------------
#(u'Statistics', None)				0
#(u'Page Visits:', u' 8663 ')		1
#(u'Submissions:', u' 10')			2
#(u'Comments Received:', u' 1856')	3
#(u'Comments Given:', u' 2264')		4
#(u'Journals:', u' 11')				5
#(u'Favorites:', u' 897')			6
#------------------------------------

#Used to hold a single user's info, saved here before writing. 
localUserList = [] 

#Takes in a line from the profile, translates the string into
#regex and adds it to our data sets
def scrape (line, lineCount, localUserList):
	if(lineCount != 0): 
		strline = str(line)
		#Handy dandy resub strips all char leaving just the int! Dynamic!
		strline = re.sub("\D", "", strline)
		localUserList.append(strline)
	return; 

#Takes in a list of HTML lines, translates them to the format needed
#for the funtion scrape. 
def translateLine(htmlList, localUserList):
	#Adding an extra line just to match it up with the format for the 
	#scrape funtion. 
	tempList = []
	tempList.append("first line statistics")
	#scrape (line, lineCount, localUserList)
	bHTML = htmlList.findAll('td')
	statistics = bHTML[1] #Because bHTML is a list of objects
	htmlLine= str(statistics).split('\n') #breaking it up into single lns
	count = 0
	for lines in htmlLine:	
		#
		if count == 0 or count == 7 or count == 8:
			nothing = ''#These are useless lines we are trimming
		else:
			if count == 1:
				# <b title="Once per user per 24 hours" style="border-bottom: 1px dotted #888; cursor: pointer">Page Visits:</b> 4884 <br />

				#Trimming off all the extra text. 
				trimmedText = lines[94:]
				tempList.append(trimmedText)
			else:
				tempList.append(lines)

		count = count + 1
	#Now, passing it to scrape
	count = 0
	for line in tempList:
		scrape(line, count, localUserList)
		count = count + 1 
	return;
#Just to make sure that we don't lose any data if we get interupted
#odds are this is a shitty way to do it but I don't want to have to fetch data
#more than once for users. 
def saveUser (localUserList):
	count = 0
	userString = ''
	for item in localUserList:
		if(count == 6): #This is the last thing in our list. 
			userString = userString + item 
		else:
			userString = userString+str(item)+'\t'
		count = count + 1
	#Adding this to our collection of user data
	userData.append(userString)
	return;


#we are going to take in two lists, master holds 
#all known users. unchecked holds who we have not looked up yet
def getUserList ( masterUserList, uncheckedUserList):
	tempList = [x for x in masterUserList if x not in uncheckedUserList]
	return tempList;

#This funtion removes duplicates from a given list. 
def cleanListOfDuplicates(givenList):	
	seen = set()
	seen_add = seen.add
	#This is the fastest known way (for Python) to keep list order
	#and removes duplicates. 
	#http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
	return [x for x in givenList if not (x in seen or seen_add(x))]

#Fetches the user's url. 
def getUser (uncheckedUserList):
	#Grabs a user we have not worked on from user list. 
	user = uncheckedUserList.pop(0)
	#print url
	return user;

def saveData ():
	#Saving and closing our file. 
	saveFile = open(userDataFilename, 'w')
	saveFile.write("\n".join(userData))
	saveFile.close()
	return;



#Start of our main
#=========================================
#Grabs our old data
userData = findUnscrapedUsers()
#Grabs our unprossesd users
uncheckedUserList = getUserList(masterUserList, uncheckedUserList)
#Looping!
count = 0 
for i in range(0, 10000): #Run this many times
	#Save the data at the start, hopefully this will avoid any crazy problems that can come about from saving half way. Save every new name we find, the socket can close kinda randomly on a slow connection. TODO change to like every 10 or 100 accounts to speed this up. 		
	saveData ()
	
	localUserList = [] 
	#get a username!
	user = getUser(uncheckedUserList)
	url = 'http://www.furaffinity.net/user/'+user+'/'
	print url
	#fetching HTML
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)
	#Moving into the ldot class
	ldotClass = soup.find('td',attrs={'class' : 'ldot'})
	if(ldotClass == None):
		print "      "+user+"'s profile is disabled."
		userString =user+'\t'+'Profile is disabled'
		userData.append(userString)

	else:
		tdHTML = 'null'
		#Moving to the second <td> tag set in the ldot class. 
		try:
			#Moving into the ldot class
			ldotClass2 = soup.findAll('td',attrs={'class' : 'ldot'})
			count = 0
			localUserList.append(user)
			#We only need the second td element. 
			row = ldotClass2[1]
			translateLine(row, localUserList)
			saveUser(localUserList)
		except:
			sys.exit("User hit EXCEPT, program break.")
#=========================================
