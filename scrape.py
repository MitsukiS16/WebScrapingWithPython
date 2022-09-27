from pdb import line_prefix
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
from csv import reader
from selenium.webdriver.support.select import Select
from datetime import date

import time
import requests
    
def my_createDataBase():

    with open("urlDBaz.txt") as dbfile:
        contList = dbfile.readlines()

    # Create DataBase

    url = "https://www.cardmarket.com/en/YuGiOh/Products/Singles?mode=list&idCategory=5&idExpansion=0&searchString=ab&idRarity=0&perSite=20"

    page = requests.get(url)

    soup = BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div',class_="row no-gutters")

    nCards = 0


    # DB with a or w
    with open('cardDBaz.csv','a',encoding='utf8',newline='') as csvfile:
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
                