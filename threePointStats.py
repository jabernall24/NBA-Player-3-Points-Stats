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
    overthrow = table.find('div', class_ = 'overthrow table_container')
    games_table = overthrow.find('table', id = 'pgl_basic')
    rows = games_table.find_all('tr')

    stats = []
    args = (
        ('strong',),
        ("td", {'data-stat' : 'fg3'}),
        ('td', {'data-stat' : 'fg3a'})
    )
    
    for row in rows:
        game_stat = []
        for arg in args:
            ele = row.find(*arg)
            game_stat.append(ele.text if ele else 0)
        if any(game_stat):
            stats.append(game_stat)

    print("Game\tMade\tTaken")
    for games, made, taken in stats:
        print(str(games) + "\t" + str(made) + "\t" + str(taken))

def compose_url(player, year):
    url = "https://www.basketball-reference.com/players/{}/{}{}01/gamelog/{}"
    first, last = player.lower().split()
    return url.format(last[0], last[:5], first[:2],year) 

def main():
 #   player = input("What player would you like to know the three point stats for: ")
 #   year = input("What year(btw: 1967 and now): ")
    player = sys.argv[1] + " " + sys.argv[2]
    year = sys.argv[3]
            
    url = compose_url(player, year)
    threePointStats(url)
  
if __name__== "__main__":
  main()
