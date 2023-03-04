# Examples of websites
#https://www.cardmarket.com/en/YuGiOh/Products/Singles?mode=list&idCategory=5&idExpansion=0&searchString=__&idRarity=0&perSite=20
#https://www.cardmarket.com/en/YuGiOh/Products/Singles?mode=list&idCategory=5&idExpansion=0&searchString=__&idRarity=0&site=2




def my_createDataBaseURL(): 
  with open('urlDB.txt', 'w') as f:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    number = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15']

    firstPart = "https://www.cardmarket.com/en/YuGiOh/Products/Singles?mode=list&idCategory=5&idExpansion=0&searchString="
    lastPart = "&idRarity=0&perSite=20"
    secondPart = "&idRarity=0&site="

    # ends in 1
    for i in alphabet:
      for j in alphabet:
        f.writelines(firstPart + i + j + lastPart + "\n")

    # other
    for i in alphabet:
      for j in alphabet:
        countOneFift = 0
        for num in number:
          f.writelines(firstPart + i + j + secondPart + num + "\n")
        
