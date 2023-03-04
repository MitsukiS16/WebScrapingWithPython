from concurrent.futures import thread
from lib2to3.pgen2 import driver
from pdb import line_prefix
from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
from csv import reader
from selenium.webdriver.support.select import Select
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import requests
    
def my_createDataBaseCards(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div',class_="row no-gutters")

    nCards = 0
    lastURLSmalller = 0

    nURL = 14

    # DB with a or w
    with open('cardDB.csv','a',encoding='utf8',newline='') as csvfile:
        thewriter = writer(csvfile)

        header = ['Deck','Title'] 
        thewriter.writerow(header)

        # Program Create DataBase

        for list in lists:

            # create for, when one ncards == 0, break many count

            deck = list.find('a',class_="yugiohExpansionIcon")

            title = list.find('div',class_="col-10")
            
            #lowerprice = list.find('div',class_="col-price pr-sm-2")
           # datetime = date.today()

            if deck is not None: 
                deck = list.find('a',class_="yugiohExpansionIcon").text

            if title is not None: 
                title = list.find('div',class_="col-10").text

            #if lowerprice is not None: 
           #    lowerprice = list.find('div',class_="col-price pr-sm-2").text

            info = [deck,title]
           # info = [deck,title,lowerprice,datetime]
            
            if deck != None:
                thewriter.writerow(info)
                nCards = nCards + 1
                    #lastURLSmalller = lastURLSmalller + 1
            #lastURLSmalller = 1
        

        print(nCards)        
   
                

