#===================================================================================================
# By: Jacob Rust
# Date: 1/17/2022
#This is a program written for Bingobeater.com to beat their numerical boards
#===================================================================================================
#IMPORTS
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
import selenium.webdriver.support.ui as WebDriverWait
import time
import os
import pandas as pd
import threading
import schedule
import datetime
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


#===================================================================================================
#INITIALIZE THINGS
history = ['free!','new','']
y = True
browser = webdriver.Firefox()
alert = Alert(browser)
board_count = 0

#===================================================================================================
#OBTAIN DIMENSIONS AND LINK
print('Enter the link for the board: ')
board_link = 'https://bingobaker.com#ea0da785bc057b94' #input()
browser.get(board_link)

generate_card = browser.find_element_by_xpath('//*[@id="disable-me"]')
generate_card.click()

ok_button = browser.find_element_by_xpath('//*[@id="ok-button"]')
ok_button.click()

#===================================================================================================


while y == True:
    print('Input the word or number that was just called: ')
    my_input = input()

    if my_input == 'q':
        break

    if my_input == 'new':
        print('New Board')
        break

    if my_input != 'new':

        try:
            s = browser.find_element_by_xpath(f"//*[contains(text(),'{my_input}')]")
            s.click()
            history.append(s.text)
            print(history)
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass






#===================================================================================================
#===================================================================================================
#===================================================================================================
#===================================================================================================
#===================================================================================================
#===================================================================================================
#TESTING AREA


'''browser = webdriver.Firefox()
alert = Alert(browser)
board_count = 0

#===================================================================================================
#OBTAIN DIMENSIONS AND LINK
print('Enter the link for the board: ')
board_link = 'https://bingobaker.com/#611075' #input()
browser.get(board_link)
generate_card = browser.find_element_by_xpath('//*[@id="disable-me"]')
generate_card.click()


ok_button = browser.find_element_by_xpath('//*[@id="ok-button"]')
ok_button.click()



#box_1 = browser.find_element_by_xpath('')
#box_1.click()

s = browser.find_element_by_xpath("//*[contains(text(),'Free!')]")
time.sleep(1)
s.click()
time.sleep(1)
x = "basketball"
b = browser.find_element_by_xpath(f"//*[contains(text(),'{x}')]")
#b = browser.find_element_by_xpath("//*[contains(text(),'Kids') and contains(text(),'')]")
print(b.text)
b.click()

#/html/body/div[2]/svg/g[2]/g/text
#/html/body/div[2]/svg/g[2]/g/text/tspan



#===================================================================================================
'''

'''''
#===================================================================================================
#Functions
def switch_tabs(site):
    browser.switch_to_window(site)
def get_items(board_dimension):


    if(board_dimension == '3'):

        var = 6
        while(var <  15):

            element_text = browser.find_element_by_css_selector("g.rect:nth-child(" + str(var) + ") > g:nth-child(1) > text:nth-child(3) ").text
            board_items.append(element_text)
            s
            var=var+1

        #print(board_items)

    if(board_dimension == '4'):
        element_text = browser.find_element_by_css_selector(f"g.rect:nth-child(7) > g:nth-child(1) > text:nth-child(3) ").text
        board_items.append(element_text)


        var = 8
        while(var <  23):

            element_text = browser.find_element_by_css_selector("g.rect:nth-child(" + str(var) + ") > g:nth-child(1) > text:nth-child(3) ").text
            board_items.append(element_text)

            var=var+1

        #print(board_items)

    if(board_dimension == '5'):
        element_text = browser.find_element_by_css_selector(f"g.rect:nth-child(8) > g:nth-child(1) > text:nth-child(4)").text
        board_items.append(element_text)

        var = 9
        while(var < 33):

            element_text = browser.find_element_by_css_selector("g.rect:nth-child(" + str(var) + ") > g:nth-child(1) > text:nth-child(3)").text
            board_items.append(element_text)
            var=var+1
def add_all_previous_answers():
    for answer in history:
        if answer in board_items:
            index = board_items.index(answer)
            select_item = browser.find_element_by_css_selector(fivebyfive[index])
            select_item.click()
            print('Clicked on box')
        else:
            print('No')
        #print(board_items)
#===================================================================================================
#SET UP
get_items(str(board_dimension))
print(history)
add_all_previous_answers()

#===================================================================================================
#Main Loop
while(y == True):

    print(history)


    print('Input the word or number that was just called: ')
    bingo_input = input()
    if bingo_input != 'new':
        if str(bingo_input) not in history:
               history.append(bingo_input)


    if(bingo_input in board_items):
        index = board_items.index(bingo_input)
        select_item = browser.find_element_by_css_selector(fivebyfive[index])
        select_item.click()
        board_count = board_count + 1

    if(bingo_input not in board_items):
        print('Not on the board')

    if(bingo_input == 'new'):
        menu_button = browser.find_element_by_xpath('//*[@id="menu-expander"]')
        menu_button.click()
        new_button = browser.find_element_by_xpath('//*[@id="new-card"]')
        new_button.click()
        Alert(browser).accept()
        time.sleep(1)
        generate_card = browser.find_element_by_xpath('//*[@id="disable-me"]')
        generate_card.click()
        ok_button = browser.find_element_by_xpath('//*[@id="ok-button"]')
        ok_button.click()

        print('================NEW BOARD====================')
        board_items = []
        get_items('5')
        board_count = 0
        add_all_previous_answers()


    if(bingo_input == 'q'):
        break



'''
#===================================================================================================
#CSS REFERENCE
'''
=====3x3====
[g.rect:nth-child(6) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(7) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(8) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(9) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(10) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(11) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(12) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(13) > g:nth-child(1) > text:nth-child(3) ,
g.rect:nth-child(14) > g:nth-child(1) > text:nth-child(3) ]
====4x4====
g.rect:nth-child(7) > g:nth-child(1) > text:nth-child(4)
g.rect:nth-child(8) > g:nth-child(1) > text:nth-child(3)
g.rect:nth-child(9) > g:nth-child(1) > text:nth-child(3)
...
g.rect:nth-child(22) > g:nth-child(1) > text:nth-child(3)
====5x5====
fivebyfive = ['g.rect:nth-child(8) > g:nth-child(1) > text:nth-child(4) ',
'g.rect:nth-child(9) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(10) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(11) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(12) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(13) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(14) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(15) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(16) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(17) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(18) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(19) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(20) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(21) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(22) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(23) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(24) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(25) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(26) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(27) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(28) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(29) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(30) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(31) > g:nth-child(1) > text:nth-child(3) ',
'g.rect:nth-child(32) > g:nth-child(1) > text:nth-child(3) ']'''

#===================================================================================================
''
