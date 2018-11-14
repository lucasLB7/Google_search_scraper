from bs4 import BeautifulSoup
import requests 
from urllib.request import urlopen
import psycopg2
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search
print("Enter Keywords or search phrase") 
query = input()
print("Enter the number of pages you want to go through")
page_num = int(input())
# conn = psycopg2.connect("dbname='google_crawl' user='postgres' password='postgres'")
try:
    for j in search(query, tld="co.in", num=page_num, stop=1, pause=2):
        search = j
        page = urlopen(search)
        soup = BeautifulSoup(page, 'html.parser')
        with open('results.html', "w") as file:
            file.write(str(soup))
except:
    pass
    
    
    
    
    
    
    
    
    
    
    # url = input(j)
    # r = requests.get("http://"+url)
    # data = r.text
    # soup = BeautifulSoup(data)

    # for link in soup.find_all('a'):
    #     print(link.get('href')) 

