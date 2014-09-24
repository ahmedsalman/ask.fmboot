import pickle
import os
import urllib2
import time
from random import randrange

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AskPoster():

    def __init__(self):
        self.base_url = "http://ask.fm/"
        self.user_list = ['Gonzalez', 'Carter', 'Nelson', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Smith', 'Collins','Johnson', 'Williams', 'Jones', 'Brown','Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson' , 'Thomas','Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Green', 'Adams', 'Baker' ]

        self.ask_user_url_list = []

        self.posts = [
        "Will you please like my facebook page. add page ulr",
        "like this facebook page add page ulr and get 20 likes",
        "Plese like my facebook page add page ulr",
        "Plese like my facebook page add page ulr and get 20 ask likes",
        "like this facebook page add page ulr and keep updated with all latest tvshowz",
        "like this facebook page add page ulr and keep updated with all latest tvshowz"
        ]

        return None


    def get_webpage(self, url):
        try:
            print url
            c = urllib2.urlopen(url)
            return c
        except Exception, e:
            print "error is ",e
            print "could not open url",url
            return None


    def login_with_facebook( self ):

        driver = webdriver.Firefox()
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_elements_by_css_selector(".link-login")[0].click()
        time.sleep(2)
        driver.find_elements_by_css_selector(".logBox_service-facebook")[0].click()

        usr = "username"
        pwd = "password"

        elem = driver.find_element_by_id("email")
        elem.send_keys(usr)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.find_elements_by_css_selector("#main_menu_search")[0].click()
        time.sleep(2)

        for search in self.user_list:
            elem = driver.find_element_by_id("q")
            elem.send_keys(search)
            elem.send_keys(Keys.RETURN)
            time.sleep( randrange(3,10) )
            count = len(driver.find_elements_by_css_selector(".link-name"))
            for x in range( 0, count ):
                try:
                    driver.find_elements_by_css_selector(".link-name")[x].click()
                except:
                    continue
                time.sleep( randrange(1,10) )
                elem = driver.find_element_by_id("profile-input")
                elem.send_keys(self.posts[randrange(0,5)])
                driver.find_element_by_id("question_submit").click()
                time.sleep( randrange(1,5) )
                driver.back()
            elem = driver.find_element_by_id("q")
            elem.clear()

obj = AskPoster()
obj.login_with_facebook()
