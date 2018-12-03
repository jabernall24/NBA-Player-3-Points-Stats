import requests
from bs4 import BeautifulSoup as bs
import sys

def threePointStats(url):
    try:
        html = requests.get(url).text
    except:
        print("Unable to parse your request")
        sys.exit()

    doc = bs(html, "html.parser")

    table = doc.find('div', id = 'all_pgl_basic')
    mclass = table.find('div', class_ = 'overthrow table_container')
    games_table = mclass.find('table', id = 'pgl_basic')
    rows = games_table.find_all('tr')

    games = []
    three_pointers_made = []
    three_pointers_taken = []
    for row in rows:
        game = row.find_all('strong')
        for t in game:
            games.append(t.text)
        
        threesMade = row.find_all('td', {'data-stat' : 'fg3'})
        for t in threesMade:
            three_pointers_made.append(t.text)

        threesTaken = row.find_all('td', {'data-stat' : 'fg3a'})
        for t in threesTaken:
            three_pointers_taken.append(t.text)

    print("Game\tMade\tTaken")
    for games, made, taken in zip(games, three_pointers_made, three_pointers_taken):
        print(games + "\t" + made + "\t" + taken)

def compose_url(player, year):
    url = "https://www.basketball-reference.com/players/{}/{}{}01/gamelog/{}"
    first, last = player.lower().split()
    return url.format(last[0], last[:5], first[:2],year) 

def main():
    player = input("What player would you like to know the stats three point stats for: ")
    year = input("What year(btw: 1967 and now): ")
            
    url = compose_url(player, year)
    threePointStats(url)
  
if __name__== "__main__":
  main()
