from selenium import webdriver

browser = webdriver.Firefox()
browser.get('Web address')

elm = browser.find_element_by_css_selector('enter css selector')

elms = browser.find_element_by_css_selector('p') #this returns alal paragraph elements

#this can be done for ids, class names, tag names , etc.

#Type into webpage
searchElem = browser.find_element_by_css_selector('.search-field') #this is the unique css selector
searchElem.send_keys('Input')
searchElem.submit() #submits input

browser.back() #goes back on webpage
#other includes forward, refresh, quit

