from __future__ import division
import fileinput
import requests
import time
import os.path
import random
from BeautifulSoup import BeautifulSoup
#=========================================
loopCount = 10000
confidencePercentage = .25 #What % we need inorder to save the account. 
#-----------------------------------------------------------
#Everything below handles how likely we think an account has free art

#We are running off a point system with a set of turns with values
totalPoints = 0
count = 0 
keyWorldListJournal = {'art' : 5,'free' : 15,'experimental' : 3,
'practice' : 10,'studies' : 5,'freebie':20,'ref':5,'test':5,
'requests':20, 'request':20, 'study':10, 'complimentary': 20}

keyWorldListJournalSize = len(keyWorldListJournal)
#-----------------------------------------------------------
#Everything here holds our lists used. 

#File information: 
filename = "userlist.txt"
saveToFileName = "freeartusers.txt"
#Array information:
userDataList = [] #List, holds all raw users from the file. 
savedUsers = [] 
#=========================================
#Checking to see if our file exists. 
doesFileExist = os.path.isfile(saveToFileName)

if doesFileExist == True:
	print "userlist.txt opened"
	with open(filename) as file:
		userDataList = file.read().splitlines()
		file.close()
elif doesFileExist == False:
	sys.exit("userlist file does not exist, quitting")

else:
	sys.exit("Something blew!!")

#Takes in our userlist and grabs a random name. 
def getUser(userList):
	user = random.choice(userList)
	return user

def createURL(user):
	url = 'http://www.furaffinity.net/user/'+user+'/'
	print "==================================================="
	print url
	return url

#Checks our user's FA journal, if there is free art 
#return true, else return false. 
#Grabs the HTML code and returns a TODO
def checkJournal(url):
	global count
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)
	journal = soup.find('div',attrs={'class' : 'no_overflow alt1'})
	postDates = soup.findAll('span',attrs={'class' : 'popup_date'})
	profileInformation = soup.find('td',attrs={'class' : 'ldot'})

	try:
		#Moving to the date in the result set. 
		journalDate = postDates[2]
		submissionDate = postDates[0]
		if((checkDate(journalDate)) == True):
			#Checking to see if there is a match in the text for ree art
			if(checkJournalContent(journal) == True):
				#Passing our URL to be saved.
				savedUsers.append(url)
				saveData()
		else:
			print "     Journal too old."
		print "--------Checking profile--------"
		if((checkDate(submissionDate)) == True):
			#Honestly, if they have not posted a submission in
			#the last 30 days, checking their profile might be useless.
			if(checkProfileContent(profileInformation) == True):
				savedUsers.append(url)
				print "     Saving account!"
				saveData()
		else:
			print "No submission in the last 30 days."
	except:
		print "     Account disabled."


#Checks to see if the profile has requests open on it.
#returns true if above precentage check val
def checkProfileContent(profileInformation):
	global count
	#Looking for "request" in the profile text. 
	profileInformation = str(profileInformation).lower()
	if "request" in profileInformation:
		#partition the profile info. 
		before_keyowrd, keyword, after_keyword = mystring.partition('request')
		#Grabbing the 50 char after the keyterm
		after_keyword = after_keyword[:50]
		if "open" in after_keyword:
			print "     Requests are open"
			count = count + 30
		if "maybe" in after_keyword:
			print "     Requests are maybe open"
			count = count + 15
		if "close" in after_keyword:
			print "     Requests are closed"
			#zootopia was really great =D
		else:
			print "     We don't know if they are open/closed for requests."
	else:
		print "     We don't know if they are open/closed for requests."
	percentageCheck = count / totalPoints
	if(percentageCheck >= confidencePercentage):
		return True;
	else:
		return False;

#Here is a funtion that finds our total points just so we don't have
#to do it by hand. 
def getTotalPoints(totalPoints):
	for key in keyWorldListJournal:
		totalPoints = totalPoints + keyWorldListJournal[key]
	totalPoints = totalPoints + 30 #Adding 50 if "requests are open" is found in their profile
	return totalPoints

#This method checks to see if the journal passed matches within a 
# % of the set word lsit. 
def checkJournalContent(journal):
	global count
	superString = ""

	for key in keyWorldListJournal:
		if key in str(journal):
			superString = superString +" "+key
			count = count + keyWorldListJournal[key]

	percentageCheck = count / totalPoints
	if(count == 0):
		print "     No keyterms found."
		return False;
	else:
		print "     ["+superString+"]"
		print "     We are about "+"{:.0%}".format(percentageCheck)+" sure."

		if(percentageCheck >= confidencePercentage):
			return True;
		else:
			return False;

def saveData():
	#Saving and closing our file. 
	saveFile = open(saveToFileName, 'w')
	saveFile.write("\n".join(savedUsers))
	saveFile.close()
	return;


#Checks the date, if it is in the last month return true, else false
def checkDate(journal_date):
	currentyear = time.strftime("%Y")
	journal_date = str(journal_date)
	journal_date = journal_date[13:]
	journal_date = journal_date[:14]

	#from this point on we have a "Mmm ddth, yyyy" format. 
	year = int(journal_date[9:])
	month = journal_date[:6]
	month = month[:3]
	day = journal_date[4:]
	day = day[:2]

	if(int(year) != int(currentyear)):
		return False;
	else:
		return checkLast30Days(month, day)

#Hashmap for our months, dat loopup time. 
months = {"Jan" : 1, "Feb" : 2, "Mar" : 3,"Apr" : 4,"May" : 5,
"Jun" : 6,"Jul" : 7,"Aug" : 8,"Sept" : 9,"Oct" : 10, "Nov" : 11, "Dec" : 12}
#Translates month from "feb" to 2 and returns it
def textMonthToNumber(month):
	try:
		numMonth = months[month]
	except:
		print "Break, error with checking the months."
	return numMonth;

def checkLast30Days(month, day):
	currentmonth = time.strftime("%m")
	currentday = time. strftime('%d')
	month = textMonthToNumber(month)

	#Checking our month. 
	if(int(currentmonth) != int(month)):
		if((int(currentmonth)) -1 != int(month)):
			return False;

	#Checking to see if the date is one digit long by abusing a 
	#try/except statement. 
	try: 
		int(day) + 0
	except:
		day = day[:1]
	#We are now going to find the number days that has passed
	#Month = 30 days because lazy.
	totalCurrentDays = (int(currentmonth) * 30) + int(currentday)
	totalJournalDays = (int(month) * 30) + int(day)
	daysApart = totalCurrentDays - totalJournalDays
	
	#Now we check if these numbers are 30 days apart. 
	if(daysApart <= 30):
		return True;
	else:
		return False;


#The "main" of our program. 
#====================================================
totalPoints = getTotalPoints(totalPoints)

for i in range(0, loopCount):
	#try:
	url = createURL(getUser(userDataList))
	checkJournal(url)
	count = 0
	#except:
		#If we get a socket refused connection error
	#	print "\n \n \n  Socket refused connect, retrying.\n \n \n "

saveData()
#====================================================
