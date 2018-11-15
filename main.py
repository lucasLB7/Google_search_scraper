from google_search import scrape_data
import sys
from colorama import init
import socket
from colorama import init
import requests
import os.path
import time

host = socket.gethostname()
IPAddr = socket.gethostbyname(host)

init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('Google spider!', font='colossal'),
       'red', 'on_grey', attrs=['bold'])

print("welcome, you are logged in as: " + host)
print("Your current IP is: " + IPAddr)

IPbucket = 0
IPlist = []


print("---------------------------------------------------------------------------")

scrape_data()
