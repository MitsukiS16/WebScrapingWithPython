# Examples of websites
#https://www.cardmarket.com/en/YuGiOh/Products/Singles/Photon-Hypernova/Bystial-Baldrake

from pandas import *
import csv


#def my_createDataBaseURL(): 

deckName = []
cardName = []

with open('cardDB.csv', 'r') as f1:
    csv_reader = csv.reader(f1, delimiter=';')
    for row in csv_reader:
        deckName.append(row[1])
        cardName.append(row[2])


with open('urlSingles.txt', 'w') as fp:
    for item1,item2 in zip(deckName,cardName):

        fp.write("https://www.cardmarket.com/en/YuGiOh/Products/Singles/")
        fp.write("%s/" %item1)
        fp.write("%s" %item2)
        fp.write("\n")
    

    print('Done')


#  with open('urlSingles.txt', 'w') as f:
#
#    firstPart = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/"
#    secondPart = list2
#    thirdPart = name card
#
#    for(i in namecard):
#        f.writeline(firstPart + secondPart + thirdPart + "\n")

