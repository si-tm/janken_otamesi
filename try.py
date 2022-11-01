import sys
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# selenium                     3.141.0

def sousa_janken():
    driver = webdriver.Chrome()
    driver.get('https://s-shinomoto.com/janken/japanese.html')
    elemr = driver.find_element_by_class_name("rock")
    elems = driver.find_element_by_class_name("scissors")
    elemp = driver.find_element_by_class_name("paper")  

    while True:
        choice = input()
        if choice == 'r':
            elemr.click()
        elif choice == 's':
            elems.click()
        elif choice == 'p':
            elemp.click()
        else:
            exit()

    driver.close()

def main():
    sousa_janken()

if __name__ == "__main__":
    main()
