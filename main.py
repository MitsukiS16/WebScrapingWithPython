from createDataBaseURL import my_createDataBaseURL
from duplicateDataBase import my_duplicateDataBase
from createDataBaseCards import my_createDataBaseCards

import time

start_time = time.time()



# idea1 - Se atualizar urlDB fica mais rapido programa
# idea2 - Atualizo, checkando 1 se tem algo na pagina se nao avança
# idea3 - Eliminate row with deck title lowerprice datetime

my_createDataBaseURL()
with open("urlDBsmall.txt") as f:
    for line in f:
        line = line.replace("\n","")
##        print(line)
        my_createDataBaseCards(line)
my_duplicateDataBase()



print("--- %s seconds ---" % (time.time() - start_time))
# TIME -> data base url - 1 url -> demora 2.9 secs
# TIME -> data base url - urlDBaz (~30lines) -> demora 10 secs
# TIME -> data base url - urlBDsmal (~600lines) -> demora 228 secs
# TIME -> data base url - urlBD (~10000lines) -> demora ??? secs