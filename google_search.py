from bs4 import BeautifulSoup
import requests 
from urllib.request import urlopen
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search
print("Enter Keywords or search phrase") 
query = input()
  
for j in search(query, tld="co.in", num=10, stop=1, pause=2):
    search = j
    page = urlopen(search)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    
    
    
    
    
    
    
    
    
    
    # url = input(j)
    # r = requests.get("http://"+url)
    # data = r.text
    # soup = BeautifulSoup(data)

    # for link in soup.find_all('a'):
    #     print(link.get('href')) 

