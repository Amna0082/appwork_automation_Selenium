from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='search_form_input_homepage']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search_button_homepage']")
    RESULTS = (By.XPATH, "//*[@id='links']//*[@data-testid='result']")


sys = {
    "x_path": {
        "button": "dasdas",
         "button2": "dasdas"
    },
    "ID": {
    }
}

print(sys["x_path"]["button"])

