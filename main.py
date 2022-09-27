from createDataBaseURL import my_createDataBaseURL
from duplicateDataBase import my_duplicateDataBase
from createDataBase import my_createDataBase

import time



start_time = time.time()


#my_createDataBaseURL()

with open("urlDBaz.txt") as f:
    content_list = f.readlines()
for line in content_list:
    print(line)



my_createDataBase()
my_duplicateDataBase()


print("--- %s seconds ---" % (time.time() - start_time))
#print(nCards)