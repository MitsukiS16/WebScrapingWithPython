from createDataBaseURL import my_createDataBaseURL
from duplicateDataBase import my_duplicateDataBase
from createDataBaseCards import my_createDataBaseCards

import time

start_time = time.time()



# idea1 - Se atualizar urlDB fica mais rapido programa
# idea2 - Atualizo, checkando 1 se tem algo na pagina se nao avança

my_createDataBaseURL()
with open("urlDBsmall.txt") as f:
    for lineurl in f:
        #print(lineurl)
        line = lineurl
        my_createDataBaseCards(line)
my_duplicateDataBase()



print("--- %s seconds ---" % (time.time() - start_time))
# TIME -> data base url - 1 url -> demora 2.9 segs
# TIME -> data base url - urlDBaz (~30lines) -> demora 10.4 segs
# TIME -> data base url - urlBDsmal (~600lines) -> demora ??? segs
# TIME -> data base url - urlBD (~10000lines) -> demora ??? segs