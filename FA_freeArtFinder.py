import fileinput
import requests
import time
import os.path
from BeautifulSoup import BeautifulSoup
#=========================================
#holds all the data from userdata. 
filename = "test.txt" #TODO
saveToFileName = "freeartusers.txt"
keyWorldList = ['art','free','experimental','practice','studies',
'freebie','ref','test','requests', 'request', 'study', 'complimentary']
#List, holds all raw users
userDataList = []
#lsit, holds users we have scraped for. 
unCheckedUsers = []
#=========================================
#Checking to see if our file exists. 
doesFileExist = os.path.isfile(saveToFileName)
if doesFileExist == True:
	print "freeartusers.txt opened"
	with open(saveToFileName) as file:
		unCheckedUsers = file.read().splitlines()
		file.close()
elif doesFileExist == False:
	sys.exit("freeartusers file does not exist, quitting")
else:
	sys.exit("Something blew!! (case 1)")
if doesFileExist == True:
	print "userlist.txt opened"
	with open(filename) as file:
		userDataList = file.read().splitlines()
		file.close()
elif doesFileExist == False:
	sys.exit("userlist file does not exist, quitting")

else:
	sys.exit("Something blew!! (case 2)")

#Reusing this nifty little funtion from the profile scraper
#Takes our processed that we have read in and then compares them 
#to our users list and gets a new list of people we have not scraped. 
def findUnscrapedUsers(unCheckedUsers):
	localList = stripUsers(unCheckedUsers)
	#Grabs all the users we have not checked before. 
	unCheckedUsers = [x for x in userDataList if x not in localList]
	return unCheckedUsers;


#This takes in an array and puts just the username in a new list that it
#returns. 
def stripUsers(unCheckedUsers):
	localList = []
	#Removing everything from our unCheckedUsers list. 
	for item in unCheckedUsers:
		head, sep, tail = item.partition('\t')
		localList.append(head)
	userCount = len(localList)
	print "Found "+str(userCount)+" old users."
	return localList
	
#Takes in our uncheckeduser list, pops off the first
#name and makes a url out of it. 
def createURL(unCheckedUsers):
	user = unCheckedUsers.pop()
	url = 'http://www.furaffinity.net/user/'+"test"+'/'
	print url
	return url

#Checks our user's FA journal, if there is free art 
#return true, else return false. 
def checkJournal(url):
	scrapePage(url)

#Grabs the HTML code and returns a TODO
def scrapePage(url):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)
	journal = soup.find('div',attrs={'class' : 'no_overflow alt1'})
	#print journal
	journal_date = soup.find('span',attrs={'class' : 'popup_date'})
	checkJornalDate(journal_date)


#Checks the date, if it is in the last month return true, else false
def checkJornalDate(journal_date):
	currentyear = time.strftime("%Y")

	journal_date = str(journal_date)
	journal_date = journal_date[13:]
	journal_date = journal_date[:14]
	#from this point on we have a "Mmm ddth, yyyy" format. 
	year = journal_date[10:]
	month = journal_date[:6]
	month = month[:3]
	day = journal_date[4:]
	day = day[:2]

	#TODO
	#if(year != currentyear):
	#	return False;
	#else:
	bool30Days = checkLast30Days(month, day)


def checkLast30Days(month, day):
	currentmonth = time.strftime("%m")
	currentday = time. strftime('%d')

	#Checking to see if the date is one digit long by abusing a 
	#try/except statement. 
	try: 
		day + 0
	except:
		day = day[:1]

	#We are now going to find the number days that has passed
	#Month = 30 days because lazy.
	print currentmonth
	totalCurrentDays = (int(currentmonth) * 30) + currentday
	print totalCurrentDays

	return;




unCheckedUsers = findUnscrapedUsers(unCheckedUsers)
url = createURL(unCheckedUsers)
checkJournal(url)


#This holds the text for 
#<div class="no_overflow alt1" align="left">
#<span title="Sep 6th, 2015 04:11 AM" class="popup_date">5 months ago</span> &nbsp;&nbsp;&nbsp;<br/><br/>








