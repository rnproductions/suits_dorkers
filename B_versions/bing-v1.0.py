import requests
import random
import urllib
from bs4 import BeautifulSoup
#import os
#import sys
print(""" 
Which dork?
1.php
2.asp
3.custom
""")
choice = input("-->")
choice = int(choice)
pages = input("how many pages -->")
pages = int(pages)


header = {'user-agent': 'Moofzilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

dorks = ["php?id=", "asp?id=", "cfm?page="]

idn = random.randint(1,100)
idn2 = str(idn)

dorks2 = list(dork + idn2 for dork in dorks)
#print(dorks2)

base = "https://www.bing.com/search?q="
base2 = "&first="

dork1 = dorks2[0]
dork2 = dorks2[1]
dork3 = dorks2[2]

#print(dork1)
#print(dork2)
#print(dork3)
sites = set()
def fir():
	
    i = page = 1

    while page <= pages:
        url = base + urllib.parse.quote(dork1) + base2 + str(i)
		
		
        html = requests.get(url, headers = header)
        if html.status_code == 200:


            data = BeautifulSoup(html.text, 'html.parser')

            results = data.find('ol', {'id': 'b_results'})

            results = results.find_all('li', {'class': 'b_algo'})

        
	
            for result in results:
                link = result.find('a').attrs['href']
                sites.add(link)
		
        else:
            break
			
        i += 1
        page += 1

    #print(sites)
    with open('results.txt', 'w') as f:
        for site in sites:
            f.write("%s\n" % site)
	
	

def sec():
	
    
    i = page = 1

    while page <= pages:
        url = base + urllib.parse.quote(dork2) + base2 + str(i)
		
		
        html = requests.get(url, headers = header)
        if html.status_code == 200:


            data = BeautifulSoup(html.text, 'html.parser')

            results = data.find('ol', {'id': 'b_results'})

            results = results.find_all('li', {'class': 'b_algo'})

        
	
            for result in results:
                link = result.find('a').attrs['href']
                sites.add(link)
		
        else:
            break
			
        i += 1
        page += 1

    #print(sites)
    with open('results.txt', 'w') as f:
        for site in sites:
            f.write("%s\n" % site)

def thi():
	
	
	dork5 = input("enter dork -->")
	i = page = 1
	
	while page <= pages:
		url = base + urllib.parse.quote(dork5) + base2 + str(i)
        
		
		html = requests.get(url, headers = header)
        
		if html.status_code == 200:
			
		    data = BeautifulSoup(html.text, 'html.parser')
		    results = data.find('ol', {'id': 'b_results'})

            
			
		    results = results.find_all('li', {'class': 'b_algo'})
		    for result in results:
				
			    link = result.find('a').attrs['href']
			    sites.add(link)
		else:
			
		    break
		i += 1
		page += 1

    #print(sites)
	with open('results.txt', 'w') as f:
		
	    for site in sites:
			
		    f.write("%s\n" % site)

	
	
	
def main():
	
	if choice == 1:
		
		fir()
		
	elif choice == 2:
		
		sec()
		
	else:
		
		thi()
	
	
main()
