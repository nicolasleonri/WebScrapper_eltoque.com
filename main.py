import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def request_url(url):
    # Create a request object with the given URL and a user-agent header
    req = Request(str(url), headers={'User-Agent': 'Mozilla/5.0'})
    # Use the urlopen function to open the request object and read the contents
    web_byte = urlopen(req).read()
    # Convert the byte data to a UTF-8 encoded string
    webpage = web_byte.decode('utf-8')
    # Return the webpage string
    return webpage


def get_title_html(html):
    # Create a BeautifulSoup object with the HTML and the lxml parser
    soup = BeautifulSoup(html, 'lxml')
    # Find the article header element and the H1 title element inside it
    title = soup.find("article").find(
        "div", {"class": "article-header"}).find("h1").text
    # Return the text content of the title element
    return title


def get_date_html(html):
    # Create a BeautifulSoup object with the HTML and the lxml parser
    soup = BeautifulSoup(html, 'lxml')
    try:
        # Try to find the second paragraph element in the article header
        date = soup.find("article").find(
            "div", {"class": "article-header"}).find_all("p")[1].text
    except:
        # If the second paragraph element is not found, find the first one
        date = soup.find("article").find(
            "div", {"class": "article-header"}).find("p").text
    # Return the text content of the date element
    return date


def get_authors_html(html):
    # Create a BeautifulSoup object with the HTML and the lxml parser
    soup = BeautifulSoup(html, 'lxml')
    # Initialize an empty list to store the author names
    authors_list = []
    # Find all the <a> elements with an "author" URL and extract the author name
    for x in soup.find("article").find_all("a", {"href": re.compile("author")}):
        authors_list.append(x.find("span", {"class": "author-name"}).text)
    # Join the author names in the list into a comma-separated string
    authors = ",".join(authors_list)
    # Return the comma-separated string of author names
    return authors


def get_txt_html(html):
    # create a BeautifulSoup object from the input HTML string
    soup = BeautifulSoup(html, 'lxml')
    # find the class name of the article
    id = soup.find("article").attrs['class'][0][:-2]
    # select the second div element with this class (assuming the first is a header)
    extract = soup.find("article").find_all(
        "div", {"class": re.compile(str(id))})[1]
    # find all div elements with a class name containing "ql-align-justify"
    text = extract.find_all(class_=re.compile("ql-align-justify"))
    # create a list of the text content of each of these elements
    list = []
    for x in text:
        list.append(x.text)
    # join the list with newline characters to create the final output string
    output = "\n".join(list)
    return output


def save_to_txt(filename, list):
    # Open a new file with the given filename for writing, overwriting any existing file with the same name.
    with open(str(filename + ".txt"), "w") as text_file:
        # Loop through each string in the list, and write it to the file followed by a newline character.
        for idx, val in enumerate(list):
            if idx-1 != len(list):
                text_file.write(val)
                text_file.write("\n")
            else:
                text_file.write(val)
    # Return None, since the function only saves a file and does not return anything.
    return None


if __name__ == "__main__":
    #### PENDIENTE: probar con otras URLs ####
    #### PENDIENTE: conseguir URLs de todos los articulos ####
    webpage = request_url(
        "https://eltoque.com/diez-consejos-para-evitar-hackeos-en-tus-cuentas-de-internet")
    title = get_title_html(webpage)
    date = get_date_html(webpage)
    author = get_authors_html(webpage)
    text = get_txt_html(webpage)
    save_to_txt("aver", [title, date, author, text])
