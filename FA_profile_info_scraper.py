import fileinput
import sys
import requests
import os.path
from BeautifulSoup import BeautifulSoup

filename = "userlist.txt"
masterUserList = [] #Only nice clean no duplicate data can go here. 

#=========================================
#Checking to see if our username exists. 
doesFileExist = os.path.isfile(filename)

if doesFileExist == True:
	print "userlist.txt opened"
	with open(filename) as file:
		masterUserList = file.read().splitlines()

elif doesFileExist == False:
	sys.exit("Username file does not exist, quitting")

else:
	sys.exit("Something blew up when making the file")


#We need to build the URL
url = 'http://www.furaffinity.net/user/wafflestheraccoon/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

#How to extract values with beautifulsoup with no class

test1 = soup.find('td',attrs={'class' : 'ldot'})
print " ============================================= "
print test1.nextSibling.nextSibling.findNext('b')
test2 = test1.findNext('b')
print test2.findNext('b')
test3 = test2.findNext('b')
print test3.findNext('b')
test4 = test3.findNext('b')
print test4.findNext('b')
test5 = test4.findNext('b')
print test5.findNext('b')
print " ============================================= "
#for td in soup.find('td', {'class': 'ldot'}).parent.find_next_siblings():
#    print(b.text)





#Saving and closing our file. 
#saveFile = open(filename, 'w')
#saveFile.write("\n".join(masterUserList))
#saveFile.close()