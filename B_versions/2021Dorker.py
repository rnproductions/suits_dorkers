#! usr/bin/python3
import grequests
import random
from bs4 import BeautifulSoup

# ADD MORE HEADERS
header = {'user-agent': 'Moofzilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
# BASE BING URL
base = "https://www.bing.com/search?q="

# SECOND PART OF BING URL

base2 = "&first="


# USER INPUT FOR PAGES
def pages_q():
    global pages
    pages = int(input('how many pages? >>'))


# SET OF FINAL SITES

bing_results = []

bings = []

final_dorks2 = []

com = []

maybe = []

good = []

other =[]


def create_dorks():
    qs = input("""
    DO YOU WANT TO..    
    1.USE CUSTOM DORK    
    
          OR
    
    2.USE DORKS.TXT    
        
        """)

    q = int(qs)

    if q == 1:

        dorks3 = input("ENTER DORK >>>")

        final_dorks2.append(dorks3 + str(random.randint(1, 1000)))

    elif q == 2:

        dorks = open("dorks.txt", 'r').read().split('\n')

        for dork in dorks:
            d = dork + str(random.randint(1, 1000))

            final_dorks2.append(d)

        print(final_dorks2)


def bing_urls():
    for final in final_dorks2:

        i = page = 1

        while page <= pages:
            global url
            url = base + final + base2 + str(i)

            bings.append(url)

            i += 10
            page += 1
    #print(bings)


        

def dorker():
    
    
    global html
    html = [grequests.get(b, headers=header) for b in bings]
    wtf = grequests.map(html)
    for w in wtf:
        #print(w.text)
         data = BeautifulSoup(w.text, 'html.parser')
         results = data.find('ol', {'id': 'b_results'})
         results = results.find_all('li', {'class': 'b_algo'})
         for result in results:
             link = result.find('a').attrs['href']
             if '?' and '=' in link:  
             	bing_results.append(link)
             	print(link)

                

def bsort():
    for b in bing_results:
        if '.com' in b:
            com.append(b)
        else:
            maybe.append(b)

    for c in com:
        if 'youtube.com' or 'facebook.com' or 'google.com' not in c:
            good.append(c)
        else:
            pass

    for m in maybe:
        if '.gov' or '.edu' not in m:
            other.append(m)
        else:
            pass                                                
                
def writeurls():  
    with open('com_results.txt', 'w') as f:
        for g in good:
            f.write("%s\n" % g)
            
            
    with open('other_results.txt', 'w') as f:
        for o in other:
            f.write("%s\n" % o)
     




def main():

    pages_q()

    create_dorks()

    bing_urls()

    dorker()

    bsort()
    
    writeurls()
    
    
main()
