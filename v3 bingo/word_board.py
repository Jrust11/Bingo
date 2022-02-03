#===================================================================================================
# By: Jacob Rust
# Date: 1/17/2022
#This is a program written for Bingobeater.com to beat their numerical boards
#===================================================================================================
#IMPORTS
import shutup
import time
import os
import datetime
import sys
import selenium.webdriver.support.ui as WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
shutup.please() #Diables depreciation warnings
fivebyfive = ['g.rect:nth-child(8) > g:nth-child(1) > text:nth-child(4) > tspan:nth-child(1)',
'g.rect:nth-child(9) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(10) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(11) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(12) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(13) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(14) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(15) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(16) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(17) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(18) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(19) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(20) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(21) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(22) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(23) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(24) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(25) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(26) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(27) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(28) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(29) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(30) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(31) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)',
'g.rect:nth-child(32) > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)']
#===================================================================================================
#INITIALIZE THINGS
board_items = []
history = [''] #Keep track of words or numbers called
active = True #Means the loop will run
browser = webdriver.Firefox()
alert = Alert(browser) #Allows me to handle alerts that pop up from chrome
#===================================================================================================

#Iterates through the array to obtain every entry from a 3,4, or 5 size array
def get_items(board_dimension):


    if(board_dimension == '3'):

        var = 6
        while(var <  15):

            element_text = browser.find_element_by_css_selector("g.rect:nth-child(" + str(var) + ") > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)").text
            board_items.append(element_text)
            s
            var=var+1

        #print(board_items)

    if(board_dimension == '4'):
        element_text = browser.find_element_by_css_selector(f"g.rect:nth-child(7) > g:nth-child(1) > text:nth-child(4) > tspan:nth-child(1)").text
        board_items.append(element_text)


        var = 8
        while(var <  23):

            element_text = browser.find_element_by_css_selector("g.rect:nth-child(" + str(var) + ") > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)").text
            board_items.append(element_text)

            var=var+1

        #print(board_items)

    if(board_dimension == '5'):
        element_text = browser.find_element_by_css_selector(f"g.rect:nth-child(8) > g:nth-child(1) > text:nth-child(4) > tspan:nth-child(1)").text
        board_items.append(element_text)

        var = 9
        while(var < 33):

            element_text = browser.find_element_by_css_selector("g.rect:nth-child(" + str(var) + ") > g:nth-child(1) > text:nth-child(3) > tspan:nth-child(1)").text
            board_items.append(element_text)
            var=var+1
#Iterates through the history array and clicks all elements on the board in history
def add_all_previous_answers():
    for answer in history:
        try:
            s = browser.find_element_by_xpath(f"//*[contains(text(),'{answer}')]")
            s.click()
            print('Clicked')
        except NoSuchElementException:  #spelling error making this code not work as expected
            print('No')
            pass
        #print(board_items)
#===================================================================================================
#OBTAIN DIMENSIONS AND LINK
print('Enter the link for the board: ')
board_link =  input()#'https://bingobaker.com#1228516'#'https://bingobaker.com/#253f9e5c34d060d9'
browser.get(board_link)

print('Enter the size of the board(Example - 5): ')
board_dimension = '5'
time.sleep(1)
#Clicks the generate card button
generate_card = browser.find_element_by_xpath('//*[@id="disable-me"]')
generate_card.click()

#Clicks the ok button to confirm choice
ok_button = browser.find_element_by_xpath('//*[@id="ok-button"]')
ok_button.click()

#===================================================================================================
#SET UP
#get_items(str(board_dimension))
print(history)
#add_all_previous_answers()
#===================================================================================================

while active == True:
    print('Input the word or number that was just called: ')
    my_input = input()

    if my_input == 'q': #Quits the game
        break

    if my_input != 'new':

        try:
            s = browser.find_element_by_xpath(f"//*[contains(text(),'{my_input}')]")
            s.click()
            history.append(s.text)
            print(history)
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass

    if my_input == 'new':
        #Click Hamburger Bar
        menu_button = browser.find_element_by_xpath('//*[@id="menu-expander"]')
        menu_button.click()
        #Click New Card
        new_button = browser.find_element_by_xpath('//*[@id="new-card"]')
        new_button.click()
        #Dismiss the browser prompt
        Alert(browser).accept()
        time.sleep(1)
        #Clicks the generate card button
        generate_card = browser.find_element_by_xpath('//*[@id="disable-me"]')
        generate_card.click()
        #Clicks the ok button to confirm choice
        ok_button = browser.find_element_by_xpath('//*[@id="ok-button"]')
        ok_button.click()

        print('================NEW BOARD====================')
        board_items = [] #Clears the items on the board
        #get_items(board_dimension)
        add_all_previous_answers()
        print(history)
