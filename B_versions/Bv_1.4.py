#! usr/bin/python3
import click
import requests
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

sites = set()

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
    print(bings)


def dorker():
    for b in bings:

        html = requests.get(b, headers=header)

        if html.status_code == 200:

            data = BeautifulSoup(html.text, 'html.parser')

            results = data.find('ol', {'id': 'b_results'})

            results = results.find_all('li', {'class': 'b_algo'})

            for result in results:
                link = result.find('a').attrs['href']
                sites.add(link)
                print(link)

        with open('results.txt', 'a') as f:
            for site in sites:
                f.write("%s\n" % site)


def banner():
    click.echo(message="""
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
       
  Coded By Suitz 6 .     
""")


def main():
    banner()

    pages_q()

    create_dorks()

    bing_urls()

    dorker()


main()
