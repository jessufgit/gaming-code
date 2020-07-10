import requests
import webbrowser
from bs4 import BeautifulSoup
from string import Template
from html.parser import HTMLParser
import random

scrapedFile = open('nicolas_cage.html','w')
cageCssFile = open('nicolas_cage.css','w')
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://www.bustle.com/articles/12026-counting-down-50-of-nicolas-cages-most-ridiculous-movie-quotes-for-his-50th-birthday", headers = headers)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('div', attrs={'class': 'kn'})
quoteArray = []
cageArray = ["<img src=http://www.placecage.com/c/200/300 />", "http://www.placecage.com/200/300", "http://www.placecage.com/g/200/300", "http://www.placecage.com/gif/200/300"]

# Writes all the quotes
for row in table.findAll('p'):
    quoteArray.append(row.text)

# Generates a random number based on the length of the array which will be used for an index
randNum = random.randint(1, len(quoteArray) - 1)
randPic = random.randint(1, len(cageArray) - 1)
cagePic = cageArray[randPic]
randQuote = quoteArray[randNum]
strRandNum = str(randNum - 2)
print(randNum)
newrandQuote = randQuote.replace('.', '').replace('â', '').replace('"', '').replace(strRandNum, '').replace('', '<br>')
print(newrandQuote)

# Writes the last quote in the master list
scrapedFile.write("<html><head><link rel='stylesheet' type='text/css' href='nicolas_cage.css'> </head><body><div class='allBoxes'><div class='picBox'><img src=" + cagePic + " /></div><div class='quoteBox'><br><p>" + newrandQuote + "</p></div></div></body></html>")
cageCssFile.write("body { text-align: center; background-color: black; color: white; width: 100%;} p { font-size: 1.3em; margin: 2px; } .allBoxes { width: 80%; margin: 5% auto; display: block; padding: 10%;} .picBox, .quoteBox { } img { padding: 2%; }")
scrapedFile.close()

# So that you can see the output of the file....
filename = 'file:///whereveryousavedthefile' + 'nicolas_cage.html'
webbrowser.open_new_tab(filename)
