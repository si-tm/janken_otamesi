import sys
import webbrowser
from selenium import webdriver

def open_janken():
    url = "https://s-shinomoto.com/janken/japanese.html"
    webbrowser.open(url, 1)

def sousa_test():
    driver = webdriver.Chrome()
    driver.get('https://www.insource.co.jp/bup/middle-schedule.html')
    form = driver.find_element_by_xpath('//*[@id="search"]/input[1]')
    form.send_keys('Python')
    form.submit()
    driver.close()

#   <div class="buttons">
#     <input class="rock" type="image" value="グー" onclick="RPS(1)" src="r.jpg" />
#     <input class="scissors" type="image" value="チョキ" onclick="RPS(2)" src="s.jpg" />
#     <input class="paper" type="image" value="パー" onclick="RPS(3)" src="p.jpg" />
#   </div>

def sousa_janken():
    driver = webdriver.Chrome()
    driver.get('https://s-shinomoto.com/janken/japanese.html')
    value = element.get_attribute('value')
    print(value)
    # driver.find_element_by_name('s_image').click()
    # driver.close()

def main():
    # open_janken()
    # sousa_test()
    sousa_janken()

if __name__ == "__main__":
    main()
