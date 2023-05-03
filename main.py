import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def initiate_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    service = ChromeService(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)

    browser.maximize_window()
    browser.implicitly_wait(10)
    return browser

def print_list(list, turn_into_txt = False, search_style = False):
    for idx, val in enumerate(list):

        if turn_into_txt == True:
            text = val.text
            val = text

        if search_style == True:
            print(val.find_all("span", {"style": "color:rgb(0, 0, 0)"}))
            return

        print(idx, val)

#driver = initiate_driver()
url="https://eltoque.com/diez-consejos-para-evitar-hackeos-en-tus-cuentas-de-internet"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')

soup = BeautifulSoup(webpage, 'lxml')

#print(soup.prettify())

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
text = soup.find("article").find_all("div", {"class": re.compile(str(id))})[1].find_all(class_=re.compile("ql-align-justify"))

print_list(text, True, False)

