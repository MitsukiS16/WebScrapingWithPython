with open("urlDBaz.txt") as f:
    content_list = f.readlines()

# Create DataBase 

for line in content_list:
    url = line
    print(url)