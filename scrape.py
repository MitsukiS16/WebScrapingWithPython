from pdb import line_prefix
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
from selenium.webdriver.support.select import Select

import time
import requests


with open("abc3.txt") as f:
    content_list = f.readlines()

for line in content_list:
    url = line


    page = requests.get(url)

    soup = BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div',class_="row no-gutters")

    nCards = 0

    #create in different directory

    #with open('carding.csv','w',encoding='utf8',newline='') as f:
    with open('carding.csv','w',encoding='utf8',newline='') as file:
        thewriter = writer(file)

        #se duas linhas, ffora 
        header = ['Deck','Title','Price']
        thewriter.writerow(header)

        for list in lists:
            deck = list.find('a',class_="yugiohExpansionIcon")
            title = list.find('div',class_="col-10")
            price = list.find('div',class_="col-price pr-sm-2")

            if deck is not None: 
                deck = list.find('a',class_="yugiohExpansionIcon").text

            if title is not None: 
                title = list.find('div',class_="col-10").text

            if price is not None: 
                price = list.find('div',class_="col-price pr-sm-2").text

            info = [deck,title,price]
            
            if deck != None and price != None:
                thewriter.writerow(info)
                nCards = nCards + 1
                


 #   # check if there are lines with the same name
 #  if nCards >= 1:
 #       with open('abc3.csv','a',encoding='utf8',newline='') as file:
    #  thewriter = writer(file)
    # header = ['Deck','Title','Price']
    # thewriter.writerow(header)

    # thewriter.writerow(info)



#       next=driver.find_element_by_xpath("")
#        next.click()
#driver.close()


#if nCards > 20:
#    print("TO BIG")
#else:
#    print(nCards)

#https://www.youtube.com/watch?v=m3liwOyJPC8
# objetivo assim, ve so em 676 sites e nao em 10000sites