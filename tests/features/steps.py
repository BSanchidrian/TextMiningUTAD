from lettuce import *
import sys
sys.path.insert(0, '/home/miggy/Documents/Practica3_VDPR/verificacion')
from strings_counter import StringsCounter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@step('I have "(.*?)"')
def have_text(step, text):
    world.driver = webdriver.Firefox(executable_path='/home/miggy/Documents/Practica3_VDPR/gecko/geckodriver')
    world.driver.get("http://127.0.0.1:8000/verificacion/")
    world.element  = world.driver.find_element_by_name("input")
    world.element.send_keys(text)

@step('I press "(.*?)" button')
def press_submit(step, btn):
    world.element = world.driver.find_element_by_id(btn)
    world.element.click()

@step('I expected "(.*?)"')
def expected(step, expected_text):
    if expected_text != " ":
        html_list = world.driver.find_element_by_tag_name("ul")
        items = html_list.find_elements_by_tag_name("li")
        flag = True
        for item in items:
            if not flag:
                text = text + ", " + item.text
            else:
                text = item.text
                flag = False
        print (text)
        assert text == expected_text, \
            "Error"
    elif expected_text == " ":
        try:
            liElement = world.driver.find_elements(By.TAG_NAME, "li").size()
        except:
            liElement = 0

        assert liElement == 0, \
            "Error text size 0"

@step ('I clean the text field')
def clean_it(step):
	world.element  = world.driver.find_element_by_name("input")
	assert world.element.text == "", \
        "Fail"
