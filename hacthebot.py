from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import hashlib

# here change the port to the port u get from HTB
url = 'http://docker.hackthebox.eu:32710/'


class HackTheBot:
    def __init__(self):  # Constructor for HackTheBot class

        self.bot = webdriver.Firefox()  # object for handling firefox browser

    def attack(self):
        bot = self.bot
        bot.get(url)
        time.sleep(1)
        str = bot.find_element_by_css_selector('h3').text

        result = hashlib.md5(str.encode())
        print(result.hexdigest())
        inp = bot.find_element_by_name('hash')

        inp.clear()
        inp.send_keys(result.hexdigest())
        inp.send_keys(Keys.RETURN)
        time.sleep(0.5)
        p = 1
        while(p == 1):

            str = bot.find_element_by_css_selector('h3').text

            result = hashlib.md5(str.encode())
            print(result.hexdigest())
            inp = bot.find_element_by_name('hash')

            inp.clear()
            inp.send_keys(result.hexdigest())
            inp.send_keys(Keys.RETURN)
            time.sleep(0.5)
            test = bot.find_element_by_css_selector('p').text
            print(test)

            if(test != "Too slow!"):
                p = 0


obj = HackTheBot()
obj.attack()
