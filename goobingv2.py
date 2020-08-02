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
	
	global urls_found
	urls_found = []
	
	results_block = soup.find_all('div', attrs={'class' : 'g'})
	
	
	for result in results_block:
		link = result.find('a', href=True)
		if link:
			link = link['href']
			
			if link != '#':
				if '?' and '=' in link:
					print(link)
					urls_found.append(link)
					
	return urls_found
					


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
	global bing_results
	bing_results = []
	for b in bings:
		html = r.get(b, headers=USER_AGENT)
		soup = bs(html.text, 'html.parser')
		#results = soup.find('ol', {'id' : 'b_results'})
		results = soup.find_all('li', {'class' : 'b_algo'})
		for result in results:
	    	 link = result.find('a').attrs['href']
	    	 if '?' and '=' in link:
	    	 	bing_results.extend(link)
	    	 	print(link)
	
        

def main():
	banner()
	global dorks
	dorks_sel()
	
	print('Which search engine would you like to scrape?')
	print('1.GOOGLE')
	print('2.BING')
	choice = str(input('''
>>>'''))
	
	if choice == '1':
		for dork in dorks:
			google(dork, amount=50)
		with open('results.txt', 'a') as f:
			for u in urls_found:
				f.write("%s\n" % u)
    
	elif choice == '2':
		for dork in dorks:
			bing(dork,20)
			bing_soup(bings)
		with open('bresults.txt', 'a') as f:
			for b in bing_results:
				f.write("%s\n" % b)
    	    	 	
	else:
		print('NOT A OPTION')
		main()


main()	    