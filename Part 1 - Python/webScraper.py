# C742 - Task 1 - Part 1
# Python Web Scraper
# By Rebecca Birmingham
# January 17th, 2019

# imports of importance
import requests
from bs4 import BeautifulSoup
import bs4
import csv

# Pull the links from the specified website and put them in a list
webLink = "https://www.census.gov/programs-surveys/popest.html"

r = requests.get(webLink)
#print(r.status_code)
rawHtml = r.text

s = BeautifulSoup(rawHtml, 'html.parser')

resultsA = s.find_all("a", {"href": True})
lenResultsA = len(resultsA)

# Pull just the link and put them all into a new list
resultsHREF = []

for eachLink in range(lenResultsA):
		resultsHREF.append(resultsA[eachLink]['href'])

#print(len(resultsHREF))
	
# Add the maineSite to the front of the link if the link begins with a slash or a pound symbol - make them absolute	
lenLessDups = len(resultsHREF)

mainSite = "https://www.census.gov"

finalLinks = []

for eachLink in range(lenLessDups):
		# Modify the link if it ends with a / - remove it, just in case
		newLink = "nothing"
		if resultsHREF[eachLink][-1] == "/":
			newLink = resultsHREF[eachLink][:-1]
		else:
			newLink = resultsHREF[eachLink]
		# Modify the link if it starts with a / or #	
		if resultsHREF[eachLink][0] == "/" or resultsHREF[eachLink][0] == "#":
			#print("this")
			finalLinks.append(mainSite + newLink)
		else:
			#print("this2")
			finalLinks.append(newLink)
	
#print(len(finalLinks))	

# Remove any duplicates
dupsRemoved = list(set(finalLinks)) # a set cannot contain duplicates, so converting the list to a set and then back to a list removes the duplicates
#print(len(dupsRemoved)) 

lenDupsRemoved = len(dupsRemoved)

#Lastly, export all of the links into a CSV file
fileName = "links.csv"

with open(fileName, "w", newline='') as output:
	fileWriter = csv.writer(output, delimiter = '\n')
	#for eachLink in range(lenDupsRemoved):
	fileWriter.writerow(dupsRemoved)

print("Pulling and exporting of links complete!")
	