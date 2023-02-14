#Importing the library

from urllib import request
import sqlite3
from datetime import date
from datetime import datetime
from bs4 import BeautifulSoup

sqliteConnection = sqlite3.connect('FixedExhangeRate.db')
cursor = sqliteConnection.cursor()
# print("Successfully Connected to SQLite")


# Initializing variable
url = "https://www.bankofalbania.org/Markets/Official_exchange_rate/"
fer = BeautifulSoup(request.urlopen(url).read(),'html.parser')

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
    
        # # Queries to INSERT records.
        try:
            cursor.execute("create table currency_t(USD integer, EUR integer, Date date NOT NULL UNIQUE)")
        except:
            print("Table Exists")
        cursor.execute("INSERT INTO Currency_t (usd, eur, date) values (?, ?, ?)",(usd, eur, udate))

        # Commit your changes in the database    
        sqliteConnection.commit()
            
        # Closing the connection
        sqliteConnection.close()
        print("Updated!")
            
    except:
        print("DB NOT Updated - DUPLICATES Found!")

if __name__ == "__main__":
    exchange() 