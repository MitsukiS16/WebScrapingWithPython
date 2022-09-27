from duplicate import my_duplicateDataBase
from scrape import my_createDataBase
import time



start_time = time.time()


my_createDataBase()
my_duplicateDataBase()


print("--- %s seconds ---" % (time.time() - start_time))
#print(nCards)