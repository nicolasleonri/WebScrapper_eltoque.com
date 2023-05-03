#!/usr/bin/python

# Importing the required modules
from bs4 import BeautifulSoup
import re

# Opening the HTML file
with open('html_download.html', 'r') as f:
    
    # Reading the contents of the HTML file
    contents = f.read()
    
    # Parsing the HTML contents using BeautifulSoup
    soup = BeautifulSoup(contents, 'html5lib')
    
    # Finding and printing the title of the article
    title = soup.find("article").find("div", {"class": "article-header"}).find("h1").text
    print(title)
    
    # Finding and printing the date of the article
    date = soup.find("article").find("div", {"class": "article-header"}).find_all("p")[1].text
    print(date)
    
    # Finding and printing the name of the author(s)
    for x in soup.find("article").find_all("a", {"href": re.compile("author")}):
        print(x.find("span", {"class": "author-name"}).text)

    # Finding the ID of the article
    id = soup.find("article").attrs['class'][0][:-2]
    
    # Extracting the contents of the article and printing the emphasized text
    extract = soup.find("article").find_all("div", {"class": re.compile(str(id))})[1]
    for x in extract.find_all("p"):
        first_try = x.find_all("span", {"style": "color:rgb(0, 0, 0)"})
        
        # Code for printing the first try text
        """
        for x in first_try:
            if x is not None:
                print(x.text)
        """
        
        # Extracting and printing the emphasized text using the second try method
        second_try = x.find_all("em")
        for y in second_try:
            if y is not None:
                print(y.text)
