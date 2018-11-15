from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from psycopg2.extensions import adapt, register_adapter, AsIs
import psycopg2
import sys
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")





# to search
print("Enter Keywords or search phrase")
query = input()
mylist = []
con = None
print("Enter the number of pages you want to go through")
page_num = int(input())
id_index = 0
con = psycopg2.connect("host='localhost' dbname='google_crawl' user='crawler' password='crawl'")
cur = con.cursor()
cur.execute("CREATE TABLE Products(Id INTEGER PRIMARY KEY, website VARCHAR(20), html_code VARCHAR)")
try:
    for j in search(query, tld="co.in", num=page_num, stop=1, pause=2):
        search = j
        page = urlopen(search)
        soup = BeautifulSoup(page, 'html.parser')
        raw_soup = ("r'%s'"%(soup,))
        id_index += 1

        # def adapt_soup(soup):
        #     return AsIs("'(%s)'" % (soup))
        # register_adapter(soup, adapt_soup)


        try:

            cur.execute("INSERT INTO Products VALUES(%s, %s, %s)",[id_index, "test",raw_soup]),
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print('Error %s' % e)
            sys.exit(1)

        finally:
            if con:
                con.close()


        # with open('results.html', "w") as file:
        #     file.write(str(soup))



except:
    print("error")














    # url = input(j)
    # r = requests.get("http://"+url)
    # data = r.text
    # soup = BeautifulSoup(data)

    # for link in soup.find_all('a'):
    #     print(link.get('href'))
