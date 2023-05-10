def initiate_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    service = ChromeService(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)

    browser.maximize_window()
    browser.implicitly_wait(10)
    return browser


def print_list(list, turn_into_txt=False, search_style=False):

    list = []

    if len(list) <= 0:
        raise IndexError("Sorry, empty list")

    for idx, val in enumerate(list):

        if turn_into_txt == True:
            text = val.text
            val = text

        if search_style == True:
            # print(val.find_all("span", {"style": "color:rgb(0, 0, 0)"}))
            return

        print(val)
        list.append(val)
        print(idx, val)
    # string = " ".join(list)

    # return(string)

