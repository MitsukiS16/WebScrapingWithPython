#transformes abreviatura em extenso

import csv

deckSigla = []
cardName = []
deckSigla2 = []
deckName = []

with open('cardDB3.csv', 'r') as f1:
    csv_reader = csv.reader(f1, delimiter=',')
    for row in csv_reader:
        deckSigla.append(row[0])
        cardName.append(row[1])
        
with open('expansion.csv', 'r') as f2:
    csv_reader = csv.reader(f2, delimiter=',')
    for row in csv_reader:
        deckSigla2.append(row[0])
        deckName.append(row[1])

with open('finalURL.csv', 'w') as fp:
    for item1,item2 in zip(deckSigla,cardName):
        if(deckSigla==deckSigla2):
            fp.write("%s/" %item1)
        fp.write("%s\n" %item2)
    

    print('Done')
