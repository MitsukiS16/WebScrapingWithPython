# Examples of websites
#https://www.cardmarket.com/en/YuGiOh/Products/Singles/Photon-Hypernova/Bystial-Baldrake

from pandas import *
import csv


#def my_createDataBaseURL(): 

deckSigla = []
cardName = []

with open('cardDB3.csv', 'r') as f1:
    csv_reader = csv.reader(f1, delimiter=',')
    for row in csv_reader:
        deckSigla.append(row[0])
        cardName.append(row[1])


with open('urlSingles.txt', 'w') as fp:
    for item1,item2 in zip(deckSigla,cardName):

        fp.write("https://www.cardmarket.com/en/YuGiOh/Products/Singles/")
        fp.write("%s/" %item1)
        fp.write("%s\n" %item2)
    

    print('Done')


#  with open('urlSingles.txt', 'w') as f:
#
#    firstPart = "https://www.cardmarket.com/en/YuGiOh/Products/Singles/"
#    secondPart = list2
#    thirdPart = name card
#
#    for(i in namecard):
#        f.writeline(firstPart + secondPart + thirdPart + "\n")

