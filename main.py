from createDataBaseURL import my_createDataBaseURL
from duplicateDataBase import my_duplicateDataBase
from createDataBaseCards import my_createDataBaseCards

import time

start_time = time.time()

data_base = "urlDB.txt" ## codigo repetido
file_name = "cardDB.csv" ## codigo repetido

nLinesDataBaseURL = 0
nCards = 0
#nCardsNext = 0

# idea1 - Se atualizar urlDB fica mais rapido programa
# idea2 - Atualizo, checkando 1 se tem algo na pagina se nao avança
# idea2 - Eliminate row with deck title lowerprice datetime
# idea4 - Se o primeiro site so acrescentar uma linha, entao avança 15-1, se o segundo site acrescentar 1 linha, avança 15-2 linhas

#my_createDataBaseURL()

with open(data_base) as f:
    for line in f:
        line = line.replace("\n","")

        # print(line)
        my_createDataBaseCards(line)



my_duplicateDataBase(file_name)



print("--- %s seconds ---" % (time.time() - start_time))
# TIME -> data base url - 1 url -> demora 2.9 secs
# TIME -> data base url - urlDBaz (~30lines) -> demora 10 secs
# TIME -> data base url - urlBDsmal (~600lines) -> demora 18min
# TIME -> data base url - urlBD (~10000lines) -> demora ??? secs