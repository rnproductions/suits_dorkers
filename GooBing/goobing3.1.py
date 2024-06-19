import random 
import requests as r
from bs4 import BeautifulSoup as bs
from termcolor import cprint

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
       
  Coded By Suitz 6 .     
 '""", 'red')
def sqlmapp():
    subprocess.call(['sqlmap', '-m', 'results.txt', '--dbs', '--level=2', '--risk=2', '--random-agent', '-o'])
com = []
dorks =[]
bing_results = []
bings = []
urls_found = []
good = []
maybe = []
bad = []
edugov = []
other = []
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def dorks_sel():
    global dorks
    cprint('1.run custom dork', 'white')
    cprint('2.run standard list', 'yellow')
    cprint('3.run list from system', 'green')
    cprint('4.run 5 random dorks from list', 'blue')
    choice2 = input('>>> ')
    if choice2 == '1':
        dorks = input('enter your dork: ')
    elif choice2 == '2':
        dorks = ['item.php?id=', 'asp?cid=', 'page.php?pid=']
    elif choice2 == '3':
        get_dork_list = input('enter dork list file name: ')    
        dorks = open(get_dork_list, 'r').read().split('\n')
    elif choice2 == '4':
        get_dork_list = input('enter dork list file name: ')    
        dork_list = open(get_dork_list, 'r').read().split('\n')
        dorks = random.choices(get_dork_list, k=5)




def google(dork, amount=50):
    url = 'https://www.google.com/search?q={}{}&num={}'.format(dork, random.randint(1,500), amount)
    rs = r.get(url, headers=USER_AGENT)
    rs.raise_for_status()
    
    soup = bs(rs.text, 'html.parser')
    
    
    
    results_block = soup.find_all('div', attrs={'class' : 'g'})
    
    
    for result in results_block:
        link = result.find('a', href=True)
        if link:
            link = link['href']
            
            if link != '#':
                if '?' and '=' in link:
                    #print(link)
                    urls_found.append(link)
                    
    #return urls_found
                    


def bing(dork, pages):
    global bings
    bings = []
    i = page = 1
    while page <= pages:
        url = 'https://www.bing.com/search?q={}{}&first={}'.format(dork, random.randint(1,100), i)
        bings.append(url)
        i += 10
        page += 1
    return bings
    



def bing_soup(bings):
    
    for b in bings:
        html = r.get(b, headers=USER_AGENT)
        soup = bs(html.text, 'html.parser')
        #results = soup.find('ol', {'id' : 'b_results'})
        results = soup.find_all('li', {'class' : 'b_algo'})
        for result in results:
             link = result.find('a').attrs['href']
             if '?' and '=' in link:
                bing_results.append(link)
                #print(link)


def gsort():
    for u in urls_found:
        if '.com' in u:
            com.append(u)
        else:
            maybe.append(u)

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


def run():
    
    
    print('Which search engine would you like to scrape?')
    print('1.GOOGLE')
    print('2.BING')
    choice = str(input('''
>>>'''))
    
    if choice == '1':
        for dork in dorks:
                    google(dork, amount=50)
        gsort()

        
        print(good)
        
        
        print(other)
        
        with open('google_com_results.txt', 'a') as f:
            for g in good:
                f.write("%s\n" % g)

        with open('google_other_results.txt', 'a') as f:
            for o in other:
                f.write("%s\n" % o)
    
    elif choice == '2':
        for dork in dorks:
            bing(dork,5)
            bing_soup(bings)
        bsort()

        print(good)
        print(other)

        with open('bing_com_results.txt', 'a') as f:
            for g in good:
                f.write("%s\n" % g)

        with open('bing_other_results.txt', 'a') as f:
            for o in other:
                f.write("%s\n" % o)
                    
    else:
        print('NOT A OPTION')
        run()        


    

def main():
	banner()
	dorks_sel()
	run()
	


main()	    
