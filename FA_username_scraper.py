import fileinput
import random
import requests
import os.path
from BeautifulSoup import BeautifulSoup

filename = "userlist.txt"
masterUserList = [] #Only nice clean no duplicate data can go here. 
userFollowingArray = [] #Holds all the userlist for a single user
totalNewUsers = 0

#=========================================
#Checking to see if our file already exists
doesFileExist = os.path.isfile(filename)

if doesFileExist == True:
	print "The file already exists"
	with open(filename) as file:
		masterUserList = file.read().splitlines()

elif doesFileExist == False:
	#Creating our file
	print "The file does not exist"
	file = open(filename, "w")

else:
	print "Something blew up when making the file"

#=========================================
#FA only shows 200 results at once, we need to run this funtion 
#for every page they have. 
def scrapePage ( url, userFollowingArray ):
	#First thing we need to do is build the url
	#'http://www.furaffinity.net/watchlist/by/USERNAME/PAGE/'

	#Scraping our data
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)

	#Pattern matching to the form of:
	#<span class="artist_name">Kiriska</span>

	faWatchList = soup.findAll('span',attrs={'class' : 'artist_name'})
	tempFollowingList = [] #For just one 200 user set. 
	#Grabbing the line and trimming the string
	for line in faWatchList:
		strline = "" + str(line)
		strline = strline[26:]
		strline = strline [:-7]
		tempFollowingList.append(strline)

	#We need to check if our list is empty, if it is break from loop
	if not tempFollowingList:
		return False;
	else:
		#Dump our data to the other list
		userFollowingArray.extend(tempFollowingList)
		#empty the list
		tempFollowingList = []
		return True;
#=========================================
#This two loops run through the user's watch and watcher list
#they quit on an empty request and break. 
def grabUserWatchers (strUser, userFollowingArray):
	intPage = 0
	# "To" means this is who is watching the user
	while True:
		intPage = intPage + 1

		#Create the URL
		template = 'http://www.furaffinity.net/watchlist/'
		url = template + 'to/'+ strUser + '/' + str(intPage)
		print url

		checkBool = scrapePage( url, userFollowingArray)
		if checkBool == False:
			break
	
	intPage = 0
	# "By" means this is who the url is watching	
	while True:
		intPage = intPage + 1

		#Create the URL
		template = 'http://www.furaffinity.net/watchlist/'
		url = template + 'by/'+ strUser + '/' + str(intPage)
		print url

		checkBool = scrapePage( url, userFollowingArray)
		if checkBool == False:
			break
	return;
#=========================================
#This funtion removes duplicates from a given list. 
def cleanListOfDuplicates(givenList):	
	seen = set()
	seen_add = seen.add

	#This is the fastest known way (for Python) to keep list order
	#and removes duplicates. 
	#http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
	return [x for x in givenList if not (x in seen or seen_add(x))]
#=========================================
#this method will get a random user to work on
def getRandomUser(givenList):

	if(len(givenList) == 0):
		print len(givenList)
		return "wafflestheraccoon" #I'm the seed, kek 

	user = random.choice(givenList)
	return user

#This loop is the bread and the butter of our script
for i in range(0, 200):
	#Grabbing a user name to scrape
	strUser = getRandomUser(masterUserList)
	#Scraping
	grabUserWatchers(strUser, userFollowingArray)	
	#Clean the list from the single user.
	userFollowingArray = cleanListOfDuplicates(userFollowingArray)

	startingSize = len(masterUserList)
	#Adding to the master user
	masterUserList.extend(userFollowingArray)
	userFollowingArray = []
	masterUserList = cleanListOfDuplicates(masterUserList)
	endingSize = len(masterUserList)

	#Calc our new usernames. 
	newUsersFound = endingSize -startingSize
	print "Found "+str(newUsersFound)+" new users!"
	totalNewUsers = totalNewUsers + newUsersFound
	newUsersFound = 0

#Sorting and cleaning our list alpabetically
masterUserList.sort()
totalUsers = len(masterUserList)
print "Found a total of "+ str(totalNewUsers)+" new users. "
print "We have "+str(totalUsers)+" users!"
#Saving and closing our file. 
saveFile = open(filename, 'w')
saveFile.write("\n".join(masterUserList))
saveFile.close()
