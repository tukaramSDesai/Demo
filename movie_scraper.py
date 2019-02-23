#Author TSD
#doi 16 February 2019
#web scraper for movie

import csv
import webbrowser
#import urlopen
from bs4 import BeautifulSoup
from requests import request

movieName = input("Enter the name of your Movie\n").replace(" ","_")# '.replace' to replace the space in the word with user defined object 
#print(movieName)
url = ("https://www.rottentomatoes.com/m/"+movieName+"/reviews/")
#print(url)
#webbrowser.open_new_tab(url)
page = request("GET", url)
pageValid = page.status_code
print(pageValid)

if pageValid != 200:
    print("Enter the right movie Name")
else: 
    #print("Checking")
    # the 'review tabel' is for the inspection of all review div
    soupRev = BeautifulSoup(page.text, "html.parser")
    for rev in soupRev.find_all('div', class_='review_tabel_row'):
        for review in rev.find_all('div', class_='the_review'):
            print(review.text)