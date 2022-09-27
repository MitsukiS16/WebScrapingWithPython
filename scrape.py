from pdb import line_prefix
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
from csv import reader
from selenium.webdriver.support.select import Select
from datetime import date

import time
import requests

start_time = time.time()

#with open("urlDBsmall.txt") as f:
#    content_list = f.readlines()

#for line in content_list:

url = "https://www.cardmarket.com/en/YuGiOh/Products/Singles?mode=list&idCategory=5&idExpansion=0&searchString=ab&idRarity=0&site=2"



page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div',class_="row no-gutters")

nCards = 0
    
 
#with open('carding.csv','w',encoding='utf8',newline='') as f:
with open('cardDBaz.csv','w',encoding='utf8',newline='') as csvfile:
    thereader = reader(csvfile,delimiter=',')
    thewriter = writer(csvfile)

    header = ['Deck','Title','LowerPrice','DateTime'] 
    thewriter.writerow(header)

    # Program Create DataBase

    for list in lists:
        deck = list.find('a',class_="yugiohExpansionIcon")
        title = list.find('div',class_="col-10")
        lowerprice = list.find('div',class_="col-price pr-sm-2")
        datetime = date.today()


        if deck is not None: 
            deck = list.find('a',class_="yugiohExpansionIcon").text

        if title is not None: 
            title = list.find('div',class_="col-10").text

        if lowerprice is not None: 
            lowerprice = list.find('div',class_="col-price pr-sm-2").text


        info = [deck,title,lowerprice,datetime]
        
        if deck != None and lowerprice != None:
            thewriter.writerow(info)
            nCards = nCards + 1
                


print("--- %s seconds ---" % (time.time() - start_time))

# Check if file its not empty 
#if nCards > 20:
#    print("TO BIG")
#else:
#    print(nCards)
# if not empty keep url in databaseurl

