#Importing the library

#from urllib import request
#import sqlite3
from datetime import date
from datetime import datetime
from bs4 import BeautifulSoup
import csv

# sqliteConnection = sqlite3.connect('FixedExhangeRate.db')
# cursor = sqliteConnection.cursor()
# print("Successfully Connected to SQLite")


# Initializing variable
html = open('exchange.html').read()
fer = BeautifulSoup(html,'html.parser')

# Extracting data for article section
bodyHtml = fer.find('div', {'class' : 'mb-2'})
bodyTable = fer.find('table', {'class' : 'table'})

# Calculating result
res = bodyHtml.get_text()
tdata = bodyTable.get_text()

# Printing the result
udate=res[13:23]


date_object = datetime.strptime(udate, '%d.%m.%Y').date()
# print(type(date_object))
# print(date_object)  # printed in default format

today = date.today()

d1 = today.strftime("%d/%m/%Y")
sysdate = datetime.strptime(d1, '%d/%m/%Y').date()



clst = tdata.split()
eur = clst[15]
usd = clst[11]

eur = float(eur)
usd = float(usd)



def exchange(): 
    print("Date on Website: ",udate)
    print("Today\'s date: ",sysdate)
    print("USD :",usd," EUR:",eur)
    print("==================================")
                 
    try:       
        
        if sysdate > date_object:
            print("Not Updated!")
        else:
             print("Currency Rate Updated.")
    
       
        print("Updated!")
            
    except:
        print("DB NOT Updated - DUPLICATES Found!")
        


datadate = date_object.strftime("%Y%m%d")
datadate = int(datadate)
filedata=[eur,840,datadate]
usddate=[usd,978,datadate]
delim = ";"
temp = list(map(str, filedata))
temp2 = list(map(str, usddate))
res = delim.join(temp)
res2 = delim.join(temp2)


# Currency_Conversion_YYYYMMDD_SS.csv
#eg:Currency_Conversion_20230119_01.csv
datadate = str(datadate)

with open('Currency_Conversion_'+datadate+'_01.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    f.write(res)
    f.write('\n')
    f.write(res2)


if __name__ == "__main__":
    exchange() 