from pdb import line_prefix
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
from selenium.webdriver.support.select import Select

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

#create in different directory

#with open('carding.csv','w',encoding='utf8',newline='') as f:
with open('cardDBaz.csv','w',encoding='utf8',newline='') as file:
    thewriter = writer(file)

    #se duas linhas, ffora 

    header = ['Deck','Title','LowerPrice']
    thewriter.writerow(header)

    for list in lists:
        deck = list.find('a',class_="yugiohExpansionIcon")
        title = list.find('div',class_="col-10")
        lowerprice = list.find('div',class_="col-price pr-sm-2")

        if deck is not None: 
            deck = list.find('a',class_="yugiohExpansionIcon").text

        if title is not None: 
            title = list.find('div',class_="col-10").text

        if lowerprice is not None: 
            lowerprice = list.find('div',class_="col-price pr-sm-2").text

        info = [deck,title,lowerprice]
        
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


#https://www.youtube.com/watch?v=m3liwOyJPC8
# objetivo assim, ve so em 676 sites e nao em 10000sites